name = "CAT_azureManager"
description = "Azure Manager"
fa_icon = " fab fa-windows "
privLevel = 3 # This is a plugin ID ... to be used as a refference
publicLinks = [
  "main",
  "create_vm"
]


from plugins.CAT_azureManager import azureDesign as D
from funcs import shell as SHELL
import json
import urllib.parse

def main(request):
  return template(request)


def template(result):
  
  #try:
  D.VMsBox()
  #except:
  #  SHELL.execute(SHELL.cmdStringToList("az login --use-device-code"))
  #  return '''
  #  <div class="w3-container"> Device just logged in. <a href="main">please refresh.</a> </div>
  #  '''
  return D.css()+'''
  <div class="w3-container">
    <h1 class="blueText" >Azure Manager</h1>
    <div class="w3-container w3-col l1 m1 s1 blue"></div>
    <div class="w3-container w3-col l1 m1 s1 "></div>
    <div class="w3-container w3-col l1 m1 s1 blue"></div>
    <div class="w3-container w3-col l1 m1 s1 "></div>
    <div class="w3-container w3-col l1 m1 s1 blue"></div>
    <div class="w3-container w3-col l1 m1 s1 "></div>
    <div class="w3-container w3-col l1 m1 s1 blue"></div>
    
    <div class="w3-container">
      <h2>VM List</h2>
      
      <div class="w3-container">
      '''+ str(D.VMsBox()) +'''
      </div>
    </div>
  </div>
  '''

def create_vm(request):
  pageNo = int(request.args.get("step"))
  data = request.args.get("data")
  if data != None:
    if data == "":
      return D.create_vm(1,{})
    data = urllib.parse.unquote(data)
    return D.create_vm(pageNo,json.loads(data),request)  
  return D.create_vm(pageNo,{})
  
  
