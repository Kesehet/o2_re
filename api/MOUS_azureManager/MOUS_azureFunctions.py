from funcs import database as DB
from funcs import settings as S

def getAllTasks():
    return DB.getTasks()

def main():
    couchdb = DB.CouchDB()
    azure_vm_manager =  AzureVmManager(couchdb=couchdb)
    # Get all documents from the 'tasks' database where the task status name is 'Not Started'
    result = couchdb.search("tasks", "by_status_name", key='"Not Started"')
    documents = result.get("rows", [])
    
    for doc in documents:
        # Get the data for the VM creation task from the task document
        
        data = doc.get("value", {}).get("data",{})
        
        resource_group_name = data.get("group")+azure_vm_manager.generate_random_string(12)
        vm_name = data.get("vm_name")
        location = data.get("location")
        size = data.get("tier")
        image = "Canonical:UbuntuServer:18.04-LTS:latest"  # Replace with appropriate image for your use case
        username = azure_vm_manager.generate_random_string(12)  # Replace with appropriate username for your use case
        password = azure_vm_manager.generate_random_string(12)  # Replace with appropriate password for your use case
        
        # Update Progress
        # doc["value"]["status"]["name"] = "In Progress"
        # couchdb.update_document("tasks", doc["value"])
        
        
        # Create the VM using the Azure VM Manager
        location = azure_vm_manager.convert_location(location)
        res = azure_vm_manager.create_resource_group(resource_group_name,location)
        res = res + azure_vm_manager.create_virtual_machine(resource_group_name, vm_name, location,size, image, username, password)
        print(res)
        # Update the task status name to 'Completed'
        doc["value"]["status"]["name"] = "Completed"
        doc["value"]["description"] = doc["value"]["description"] + " The host said => "+ str(res).replace("\\","\\\\")
        
        couchdb.update_document("tasks", doc["value"])
        

	
	
class AzureVmManager:
    
    def __init__(self, couchdb):
        self.couchdb = couchdb
        self.virtualMachine_DBName = "virtual_machines"
        self.resourceGroup_DBName = "azure_resource_groups"
        self.couchdb.create_database(self.virtualMachine_DBName)
        self.couchdb.create_database(self.resourceGroup_DBName)

    def run_powershell_command(self, command):
        from funcs import shell as SHELL
        return SHELL.run("pwsh -Command "+ command)

    def create_resource_group(self, resource_group_name, location):
        '''
        This function creates a new resource group in Azure with the given name and location. It uses the Azure PowerShell command New-AzResourceGroup to create the resource group and returns the result of this command. Additionally, it creates a new document in the resourceGroup_DBName database using CouchDB, which stores the name and location of the new resource group for future reference.
        '''
        command = f"New-AzResourceGroup -Name {resource_group_name} -Location {location}"
        result = self.run_powershell_command(command)
        self.couchdb.create_document(self.resourceGroup_DBName, {"name": resource_group_name, "location": location})
        return result

    def delete_resource_group(self, resource_group_name):
        command = f"Remove-AzResourceGroup -Name {resource_group_name} -Force"
        result = self.run_powershell_command(command)
        self.couchdb.delete_document(self.resourceGroup_DBName, resource_group_name, "<rev>")
        return result

    def create_virtual_machine(self, resource_group_name, vm_name, location, size, image, username, password):
        
        # Choose the appropriate VM size based on the image type
        location = self.convert_location(location=location)
        size = self.get_best_size(location=location, image_type=size.lower())
            
        # Create the VM using the selected size
        command = f"""New-AzVm -ResourceGroupName {resource_group_name} -Name {vm_name} -Location {location} -Size {size} -PublicIpSku Standard -Zone 1 -Image {image} -Credential (New-Object System.Management.Automation.PSCredential('{username}', (ConvertTo-SecureString '{password}' -AsPlainText -Force)))"""
        print(command)
        result = self.run_powershell_command(command)
	
        # Create a public IP address
        public_ip_command = f"""New-AzPublicIpAddress -Name {vm_name}PublicIP -ResourceGroupName {resource_group_name} -Location {location} -AllocationMethod Dynamic"""
        self.run_powershell_command(public_ip_command)
	
        # Associate the public IP address with the VM's network interface
        associate_public_ip_command = f"""$vm = Get-AzVM -ResourceGroupName {resource_group_name} -Name {vm_name}; $nic = Get-AzNetworkInterface -ResourceId $vm.NetworkProfile.NetworkInterfaces[0].Id; Add-AzNetworkInterfaceIpConfig -Name {vm_name}IpConfig -NetworkInterface $nic -SubnetId $nic.IpConfigurations[0].Subnet.Id -PublicIpAddressId (Get-AzPublicIpAddress -ResourceGroupName {resource_group_name} -Name {vm_name}PublicIP).Id; Set-AzNetworkInterface -NetworkInterface $nic"""
        self.run_powershell_command(associate_public_ip_command)
        
		# Get the VM and public IP information
        get_vm_and_public_ip_command = f"""$vm = Get-AzVM -ResourceGroupName {resource_group_name} -Name {vm_name}; $publicIp = Get-AzPublicIpAddress -ResourceGroupName {resource_group_name} -Name {vm_name}PublicIP; $publicIp.IpAddress"""
        ip_address = self.run_powershell_command(get_vm_and_public_ip_command)
		
		# Return the connection information
        if "Windows" in image:
            connection_info = f"Use RDP to connect: mstsc /v:{ip_address} /u:{username} /p:{password}"
        else:
            connection_info = f"Use SSH to connect: ssh {username}@{ip_address} -p 22"
		
        # Add the VM to the virtual machine database
        self.couchdb.create_document(self.virtualMachine_DBName, {"connection_info":connection_info,"name": vm_name, "resource_group": resource_group_name, "location": location, "size": size, "image": image, "username": username, "password": password})
        
        return result + " command used was " + command + ". Connection info: " + connection_info



    def update_virtual_machine(self, resource_group_name, vm_name, size):
        command = f"""$vm = Get-AzVM -ResourceGroupName {resource_group_name} -Name {vm_name}
$vm.HardwareProfile.VmSize = '{size}'
Update-AzVM -ResourceGroupName {resource_group_name} -VM $vm"""
        result = self.run_powershell_command(command)
        self.couchdb.update_document(self.virtualMachine_DBName, vm_name, {"size": size})
        return result

    def delete_virtual_machine(self, resource_group_name, vm_name):
        command = f"Remove-AzVM -ResourceGroupName {resource_group_name} -Name {vm_name} -Force"
        result = self.run_powershell_command(command)
        self.couchdb.delete_document(self.virtualMachine_DBName, vm_name, "<rev>")
        return result

    def rename_virtual_machine(self, resource_group_name, vm_name, new_vm_name):
        command = f"""$vm = Get-AzVM -ResourceGroupName {resource_group_name} -Name {vm_name}
$vm.Name = '{new_vm_name}'
Update-AzVM -ResourceGroupName {resource_group_name} -VM $vm"""
        result = self.run_powershell_command(command)
        self.couchdb.update_document(self.virtualMachine_DBName, vm_name, {"name": new_vm_name})
        return result
    
    def get_available_vm_sizes(self, location):
        location = self.convert_location(location)
        command = f"Get-AzVMSize -Location {location}"
        output = self.run_powershell_command(command)
        # Split output by lines and remove header/footer
        lines = output.strip().splitlines()[2:-2]
        sizes = []
        for line in lines:
            # Split each line by whitespace and extract name field
            fields = line.split()
            name = fields[0]
            sizes.append(name)
        return sizes

    def get_best_size(self,location, image_type):
        #sizes = self.get_available_vm_sizes(location)
        if image_type.lower() == "Premium".lower():
            return "Standard_B1ls"
        elif image_type.lower() == "Standard".lower():
            return "Standard_B1ls"
        elif image_type.lower() == "Basic".lower():
            return "Standard_B1ls"
        else:
            return "no_size"




    def convert_location(self,location):
        location_dict = {
            "eastus": ["east us"],
            "eastus2": ["east us 2"],
            "westus": ["west us"],
            "centralus": ["central us"],
            "northcentralus": ["north central us"],
            "southcentralus": ["south central us"],
            "northeurope": ["north europe"],
            "westeurope": ["west europe"],
            "eastasia": ["east asia"],
            "southeastasia": ["southeast asia"],
            "japaneast": ["japan east"],
            "japanwest": ["japan west"],
            "australiaeast": ["australia east"],
            "australiasoutheast": ["australia southeast"],
            "australiacentral": ["australia central"],
            "brazilsouth": ["brazil south", "south brazil", "brazil southeast","brazilsouth"],
            "southindia": ["south india"],
            "centralindia": ["central india"],
            "westindia": ["west india"],
            "canadacentral": ["canada central"],
            "canadaeast": ["canada east"],
            "westus2": ["west us 2"],
            "westcentralus": ["west central us"],
            "uksouth": ["uk south"],
            "ukwest": ["uk west"],
            "koreacentral": ["korea central"],
            "koreasouth": ["korea south"],
            "francecentral": ["france central"],
            "southafricanorth": ["south africa north", "north south africa"],
            "uaenorth": ["uae north", "north uae"],
            "switzerlandnorth": ["switzerland north", "north switzerland"],
            "germanywestcentral": ["germany west central", "west central germany"],
            "norwayeast": ["norway east", "east norway"],
            "jioindiawest": ["jio india west", "west jio india"],
            "westus3": ["west us 3"],
            "swedencentral": ["sweden central", "central sweden"],
            "qatarcentral": ["qatar central", "central qatar"]
        }
        
        for key in location_dict:
            if location.lower() in location_dict[key] or location.lower() in key:
                return key
        
        raise ValueError(f"Invalid location: {location}")
    
    def generate_random_string(self,length):
        import random
        import string
        random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
        return f"-{random_string}-{''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))}-"

