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
        couchdb.update_document("tasks", doc["_id"], doc)

	
	
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
        # Get a list of available VM sizes for the specified location
        sizes = self.get_available_vm_sizes(location)
        print(sizes)
        # Choose the appropriate VM size based on the image type
        if "premium" in image.lower():
            size = self.get_best_vm_size(sizes)
        elif "standard" in image.lower():
            size = self.get_standard_vm_size(sizes)
        else:
            size = self.get_basic_vm_size(sizes)
            
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
        print(output)
        sizes = [size["Name"] for size in output]
        return sizes

    def get_best_vm_size(self, sizes):
        # Choose the VM size with the most RAM and highest number of vCPUs
        best_size = max(sizes, key=lambda size: (self.get_vm_ram(size), self.get_vm_vcpus(size)))
        return best_size

    def get_standard_vm_size(self, sizes):
        # Choose the VM size with the lowest number of vCPUs
        standard_sizes = [size for size in sizes if "standard" in size.lower()]
        standard_size = min(standard_sizes, key=lambda size: self.get_vm_vcpus(size))
        return standard_size

    def get_basic_vm_size(self, sizes):
        # Choose the VM size with the lowest amount of RAM
        basic_sizes = [size for size in sizes if "basic" in size.lower()]
        basic_size = min(basic_sizes, key=lambda size: self.get_vm_ram(size))
        return basic_size

    def get_vm_ram(self, size):
        # Extract the RAM size from the VM size string
        return int(re.search(r"\d+", size).group())

    def get_vm_vcpus(self, size):
        # Extract the number of vCPUs from the VM size string
        return int(re.search(r"vcpus=(\d+)", size).group(1))
    
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
            "brazilsouth": ["brazil south", "south brazil", "brazil southeast"],
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
            if location.lower() in location_dict[key]:
                return key
        
        raise ValueError(f"Invalid location: {location}")

