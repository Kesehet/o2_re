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
        data = doc.get("data", {})
        resource_group_name = data.get("group")
        vm_name = data.get("vm_name")
        location = data.get("cityName")
        size = data.get("tier")
        image = "default_image"  # Replace with appropriate image for your use case
        username = "default_username"  # Replace with appropriate username for your use case
        password = "default_password"  # Replace with appropriate password for your use case

        # Create the VM using the Azure VM Manager
        azure_vm_manager.create_virtual_machine(resource_group_name, vm_name, location, size, image, username, password)

        # Update the task status name to 'Completed'
        print(doc)
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

    def create_virtual_machine(self, resource_group_name, vm_name, location, size, image, username, password):
        command = f"""New-AzVm -ResourceGroupName {resource_group_name} -Name {vm_name} -Location {location} -VMSize {size} \
-Image {image} -Credential (New-Object System.Management.Automation.PSCredential('{username}', (ConvertTo-SecureString '{password}' -AsPlainText -Force)))"""
        result = self.run_powershell_command(command)
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
