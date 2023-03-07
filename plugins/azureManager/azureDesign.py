import json
from funcs import shell as SHELL
from funcs import database as DB
from plugins.azureManager import azureFuncs as A
from plugins.azureManager import azureHTMLTemplates as T
from funcs import users as U

def VMsBox():
  ret = createNewVMBox()
  vms = A.getAllVMs()
  for i in range(len(vms)):
    ret = ret + '''
    <div class="w3-container w3-third w3-padding">  
      <div class="w3-card-4 w3-hover-gray card">
      <i class="fas fa-server card-icon"></i>
      <h2 style="text-transform:capitalize;" class="dashToSpace" >'''+ vms[i]["name"] +'''</h2>
      <p>'''+'''</p>
          <div class="w3-container">
              <p><i class="fas fa-network-wired"></i> IP: '''+vms[i]["ip"]+'''</p>
              <p><i class="fas fa-circle w3-text-green '''+vms[i]["status"].split("/")[1]+''' "></i> '''+vms[i]["status"]+'''</p>
          </div>
      </div>
    </div>
  '''
  return ret
def createNewVMBox():
  return '''
      <div onclick="window.location.href = 'create_vm?step=1'" class="w3-container w3-third w3-padding">  
      <div class="w3-card-4 w3-hover-gray card">
      <i class="fas fa-plus card-icon"></i>
      <h2 style="text-transform:capitalize;" >'''+ "Create New VM" +'''</h2>
      </div>
    </div>
  '''



def create_vm(page:int,dat:dict,request=None):
  if page == 1:
    return T.create_vm_step_1("create_vm?step=2&data=[*data*]")
  if page == 2:
    return T.create_vm_step_2("create_vm?step=3&data=[*data*]",dat)
  if page == 3:
    return T.create_vm_step_3("create_vm?step=4&data=[*data*]",dat)
  if page == 4:
    data = DB.Schema().getTask("VM_CREATION","vm creation by "+U.getEmail(request),dat,0,[dat])
    DB.setRow("tasks",data)
    return "<h1>VM Creation Started.</h1>"
  return ""


def css():
  return '''
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css
">
  	<style>
    .deallocated{
      color: red !important;
    }
		.card {
			background-color: #f1f1f1;
			border-radius: 5px;
			box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
			padding: 20px;
			text-align: center;
		}
		.card-icon {
			font-size: 64px;
			margin-bottom: 20px;
		}
	</style>'''
  