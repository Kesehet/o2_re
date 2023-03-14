import json
from funcs import shell as SHELL
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient


creds = DefaultAzureCredential()
  
sub_id = "e98131a2-166d-4319-9563-07185428a204"
compute_client = ComputeManagementClient (creds,sub_id)
net_cred = NetworkManagementClient(creds,sub_id)



def getIP(VMName:str,VMResourceGroup:str):
    ret = json.loads(SHELL.execute(SHELL.cmdStringToList(
      "az vm list-ip-addresses -g "+ VMResourceGroup +" -n "+VMName
      )))[0]["virtualMachine"]["network"]["publicIpAddresses"][0]["ipAddress"]
    return str(ret)
    
def getVMStatus(VMName:str,VMResourceGroup:str):
    ret = str(SHELL.execute(SHELL.cmdStringToList('az vm show -g '+VMResourceGroup+' -n '+VMName+' --query "powerState" -o tsv')))
    print('az vm show -g '+VMResourceGroup+' -n '+VMName+' --query "powerState" -o tsv')
    return ret

def getUsageMetrics(VMName:str,VMResourceGroup:str):
    return SHELL.execute(SHELL.cmdStringToList("az vm monitor metrics list-definitions --name "+VMName+" --resource-group "+VMResourceGroup))


def getAllVMs():
  
  ret = []
  
  for vm in compute_client.virtual_machines.list_all():
    array = vm.id.split("/")
    vm_name = array[-1]
    group = array[4]
    print(vm_name)
    p_ip = net_cred.network_interfaces.get(group,vm.network_profile.network_interfaces[0].id.split("/")[-1]).ip_configurations[0].public_ip_address
    ip = net_cred.public_ip_addresses.get(group,p_ip.name)
    
    statuses = compute_client.virtual_machines.instance_view(group,vm_name).statuses
    status = len(statuses) >= 2 and statuses[1]
    stat = status.code if (status) else "Missing"
    re = vm.as_dict()
    re["resourceGroup"] = group
    re["status"] = stat
    re["ip"] = ip.ip_address
    ret.append(re)
  return ret