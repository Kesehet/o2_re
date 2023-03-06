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
from random import randint
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
    place = d["metadata"]["geographyGroup"] if d["metadata"]["geographyGroup"] != None else "" 
    fullName = name + ", "+ name2 if name2 != "" and name != "" else name
    latitude = d["metadata"]["latitude"] if d["metadata"]["latitude"] != None and d["metadata"]["latitude"] != "null" else ""
    longitude = d["metadata"]["longitude"] if d["metadata"]["longitude"] != None and d["metadata"]["longitude"] != "null" else ""
    if latitude == "" or longitude == "" or name == "" or name2 == "" or place == "":
      continue
    ret.append({
      "name":name,
      "name2":place,
      "fullName":fullName,
      "lat":latitude,
      "long":longitude
              })
  return ret