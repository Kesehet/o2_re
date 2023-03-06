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
    return str(getAllLocations())

  


def getAllLocations():
  ret = []
  dat  = json.loads(SHELL.run("sudo az account list-locations"))
  for d in dat:
    ret.append({
      "name":d["displayName"]
    })
  return dict(ret)