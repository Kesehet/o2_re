from funcs import database as DB
from funcs import settings as S
from api.MOUS_azureManager import MOUS_azureClasses as C
import threading
import time

def getAllTasks():
    return DB.getTasks()


couchdb = DB.CouchDB()
def main():
    
    azure_vm_manager =  C.AzureVmManager(couchdb=couchdb)
    # Get all documents from the 'tasks' database where the task status name is 'Not Started'
    result = couchdb.search("tasks", "by_status_name", key='"Not Started"')
    documents = result.get("rows", [])
    threads = []
    # create and start threads
    for doc in documents:
        t = threading.Thread(target=loop_thread, args=(doc,))
        t.start()
        threads.append(t)
    return str(threads)






def loop_thread(doc):
    task = doc.get("value",{})
    task_name = task.get("name","")
    updatedTaskID = updateTaskStatus(doc,1).get("id")
    if task_name == "vm_creation":
        create_vm(couchdb.get_document("tasks",updatedTaskID))
    if task_name == "vm_deletion":
        delete_vm(doc)





# main thread continues executing
print("Main thread continuing to run")

# more code here...

print("Main thread finished")









        
def updateTaskStatus(doc,status:int):
    taskNow = couchdb.get_document("tasks",doc["id"])
    taskNow["status"] = DB.Schema.getStatus(index=status)
    return couchdb.update_document("tasks",taskNow)

def create_vm(doc):
    couchdb = DB.CouchDB()
    manager =  getManager("Azure")

    data = doc.get("data",{})
    resource_group_name = data.get("group")+"-"+manager.generate_random_string(12)
    vm_name = data.get("vm_name")
    location = data.get("location")
    size = data.get("tier")
    image = "Canonical:UbuntuServer:18.04-LTS:latest"  # Replace with appropriate image for your use case
    username = manager.generate_random_string(12)  # Replace with appropriate username for your use case
    password = manager.generate_random_string(12)  # Replace with appropriate password for your use case
    
    
    
    # Create the VM using the Azure VM Manager
    location = manager.convert_location(location)
    res = manager.create_resource_group(resource_group_name,location)
    res = res + manager.create_virtual_machine(resource_group_name, vm_name, location,size, image, username, password)
    

    # Update the task status name to 'Completed'
    doc["status"] = DB.Schema.getStatus(4)
    doc["description"] = doc["description"]+" The host said =>" + res.encode('latin1').decode('unicode_escape')
    
    couchdb.update_document("tasks", doc)

def delete_vm(doc):
    rgName = doc.get("data").get("group")
    vmName = doc.get("data").get("vm_name")
    manager = getManager("Azure")
    manager.delete_virtual_machine(rgName,vmName)



def getManager(hostName = "Azure"):
    if hostName == "Azure":
        return C.AzureVmManager(couchdb)
    return C.AzureVmManager(couchdb)
