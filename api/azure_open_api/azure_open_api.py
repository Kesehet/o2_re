name = "azure_open_api"
description = "Azure Open API for sharing general details."
fa_icon = "phone"
AccessID = 0
privLevel = AccessID
isOpenToPublic = True
publicLinks = [
  "main"
]

import funcs.shell as SHELL
import json 
def main(request):
  task = request.args.get("task")
  return tasks(task)

def tasks(task):
  if task == "get-machine-by-location":
    return str(getAllLocations()).replace("&#39;",'"')

  


def getAllLocations():
  ret = []
  dat  = json.loads(SHELL.run("sudo az account list-locations"))
  for d in dat:
    name = d["metadata"]["physicalLocation"] if d["metadata"]["physicalLocation"] != None else ""
    name2 = d["displayName"] if d["displayName"] != None else "" 
    fullName = name + ", "+ name2 if name2 != "" and name != "" else name
    latitude = d["metadata"]["latitude"] if d["metadata"]["latitude"] != None and d["metadata"]["latitude"] != "null" else "0.0"
    longitude = d["metadata"]["longitude"] if d["metadata"]["longitude"] != None and d["metadata"]["longitude"] != "null" else "0.0"
    ret.append({
      "name":name,
      "name2":name2,
      "fullName":fullName,
      "lat":latitude,
      "long":longitude
              })
  return ret