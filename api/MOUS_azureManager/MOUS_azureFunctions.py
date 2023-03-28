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
        couchdb.delete_document("tasks",doc["value"]["_id"],doc["value"]["_rev"])
        resource_group_name = data.get("group")
        vm_name = data.get("vm_name")
        location = data.get("location")
        size = data.get("tier")
        image = "default_image"  # Replace with appropriate image for your use case
        username = "user"  # Replace with appropriate username for your use case
        password = "eU2CA2n@1Qmu7z9m19*"  # Replace with appropriate password for your use case

        # Create the VM using the Azure VM Manager
        res = azure_vm_manager.create_virtual_machine(resource_group_name, vm_name, location, image, username, password)
        # Update the task status name to 'Completed'
        doc["value"]["status"]["name"] = "Completed"
        doc["value"]["description"] = doc["value"]["description"] + "\n The host said => "+ str(res)
        couchdb.create_document("tasks",doc["value"])
        

	
	
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

    def create_virtual_machine(self, resource_group_name, vm_name, location, image, username, password):
        
        # Choose the appropriate VM size based on the image type
        location = self.convert_location(location=location)
        size = self.get_best_size(location=location,image_type=image.lower())
            
        # Create the VM using the selected size
        command = f"""New-AzVm -ResourceGroupName {resource_group_name} -Name {vm_name} -Location {location} -VMSize {size} \
    -Image {image} -Credential (New-Object System.Management.Automation.PSCredential('{username}', (ConvertTo-SecureString '{password}' -AsPlainText -Force)))"""
        result = self.run_powershell_command(command)
        
        # Add the VM to the virtual machine database
        self.couchdb.create_document(self.virtualMachine_DBName, {"name": vm_name, "resource_group": resource_group_name, "location": location, "size": size, "image": image, "username": username, "password": password})
        
        return result


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
        sizes = self.get_available_vm_sizes(location)
        premium_sizes = ["Standard_NC6s_v3", "Standard_NC12s_v3", "Standard_NC24rs_v3", "Standard_NC24s_v3"]
        standard_sizes = ["Standard_A1_v2", "Standard_A2m_v2", "Standard_A2_v2", "Standard_A4m_v2", "Standard_A4_v2", "Standard_A8m_v2", "Standard_A8_v2"]
        basic_sizes = ["Standard_B1ls", "Standard_B1ms", "Standard_B1s", "Standard_B2ms", "Standard_B2s", "Standard_B4ms", "Standard_B8ms", "Standard_B12ms", "Standard_B16ms", "Standard_B20ms"]
        best_size = ""
        if image_type == "Premium":
            for size in sizes:
                if size in premium_sizes:
                    best_size = size
                    break
        elif image_type == "Standard":
            for size in sizes:
                if size in standard_sizes:
                    best_size = size
                    break
        elif image_type == "Basic":
            for size in sizes:
                if size in basic_sizes:
                    best_size = size
                    break
        return best_size




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

