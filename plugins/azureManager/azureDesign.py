import json
from funcs import shell as SHELL
from funcs import database as DB
from plugins.azureManager import azureFuncs as A
from plugins.azureManager import azureHTMLTemplates as T
from funcs import users as U
from funcs import settings as S

def VMsBox():
  ret = createNewVMBox()
  vms = A.getAllVMs()
  for i in range(len(vms)):
    ret = ret + '''
    <div class="w3-container w3-third w3-padding ">  
      <div class="w3-card-4 w3-hover-gray card zoomOnHover">
      <i class="fas fa-server card-icon"></i>
      <h2 style="text-transform:capitalize;" class="dashToSpace" >'''+ vms[i]["name"] +'''</h2>
      <p>'''+'''</p>
          <div class="w3-container">
              <p><i class="fas fa-network-wired"></i> IP: '''+vms[i]["ip"]+'''</p>
              <div class="w3-tooltip" >
                  <div class="w3-container">
                    <i style="animation: fading 1.'''+str(i)+'''s infinite !important;"  class="fas fa-circle w3-animate-fading w3-text-green '''+vms[i]["status"].split("/")[1]+''' "></i> 
                    '''+vms[i]["status"]+'''
                  </div>
                  <div class="w3-container w3-text">
                      <div class="w3-col l6 m6 s12 w3-button w3-red '''+vms[i]["status"].split("/")[1]+'''-off ">
                          <i class="fa-solid fa-stop"></i>
                      </div>
                      <div class="w3-col l12 m12 s12 w3-button w3-green '''+vms[i]["status"].split("/")[1]+'''-on ">
                          <i class="fa-solid fa-play"></i>
                      </div>
                      <div class="w3-col l6 m6 s12 w3-button w3-yellow '''+vms[i]["status"].split("/")[1]+'''-restart ">
                          <i class="fa-solid fa-refresh"></i>
                      </div>
                  </div>
              </div>

          </div>
      </div>
    </div>
  '''
  return ret
def createNewVMBox():
  return '''
      <div onclick="window.location.href = 'create_vm?step=1'" class="w3-container w3-third w3-padding zoomOnHover w3-tooltip" style="overflow:hidden;">
      <div class="w3-card-4 w3-hover-gray card">
      <i class="fas fa-plus card-icon"></i>
      <h2 style="text-transform:capitalize;" >'''+ "Create New VM" +'''</h2>
      <p>'''+'''</p>
          <div class="w3-container ">
              <p>Are you ready to put your virtual carpentry skills to the test?</p>
              <p class="w3-text w3-animate-bottom" >Let's hammer out a new virtual machine and build the future of computing, one bit at a time.</p>
          </div>
      </div>
    </div>
  '''

def create_step_3_group_box(opt):
  return '''<a href="#" class="w3-bar-item w3-button w3-round-xxlarge grey" onclick="document.getElementById('group_box').innerText = \''''+opt+'''\'; ">'''+opt+'''</a>'''


def create_vm(page:int,dat:dict,request=None):
  if page == 1:
    return T.create_vm_step_1("create_vm?step=2&data=[*data*]")
  if page == 2:
    return T.create_vm_step_2("create_vm?step=3&data=[*data*]",dat)
  if page == 3:
    group_list = ["group 1" , "group 2"]
    glist = ""
    for g in group_list:
      glist = glist + create_step_3_group_box(g)
    return T.create_vm_step_3("create_vm?step=4&data=[*data*]",dat,glist)
  if page == 4:
    dat["vm_name"] = cleanStrForSave(dat["vm_name"],25)
    dat["tier"] = cleanStrForSave(dat["tier"])
    dat["group"] = cleanStrForSave(dat["group"])
    dat["descr"] = cleanStrForSave(dat["descr"])
    dat["desc"] = cleanStrForSave(dat["desc"])
    dat["cityName"] = cleanStrForSave(dat["cityName"])
    dat["place"] = cleanStrForSave(dat["place"])
    data = DB.Schema().getTask(
      "VM_CREATION",
      "The VM Creation has been requested for "+dat["vm_name"],
      dat,
      0,
      [dat],
      request
      )
    DB.setRow("tasks",data)
    next_url_is = S.Urls["plugin"].replace("<name>","tasks").replace("<functionCall>","main")
    return T.create_vm_step_4(next_url_is)
  return ""

def cleanStrForSave(string:str,truncate=-1):
  string = "".join(ch for ch in string if ch.isalnum() or ch == " " or ch == "-" or ch == "_")
  string = string.lower().replace(" ","-")
  string = string.replace("--","-").replace("__","_")
  if truncate != -1:
    string = string[0:truncate]
  return string

def css():
  return '''
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css
">
  	<style>
    .deallocated{
      color: red !important;
    }
    .running-off{
      display:block;
      color: #313946;
      background-color: #A30015;
    }
    .deallocated-off{
      display:none;
    }
    .running-on{
      display:none;
    }
    .deallocated-on{
      display:block;
      color : #313946;
      background-color: #26c485;
    }
    .running-restart{
      display:block;
      color: #313946;
      background-color: #fde74c;
    }
    .deallocated-restart{
      display:none;
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
  