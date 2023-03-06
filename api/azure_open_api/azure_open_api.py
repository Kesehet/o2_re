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
      "long":longitude,
      "desc":mockDescript(name,name2,place)
              })
  return ret

def mockDescript(city,cntry,region):
  lst = [
      "Our data center in [LOCATION_NAME], a bustling metropolis in [COUNTRY_NAME], boasts top-of-the-line technology and infrastructure, providing exceptional cloud services for businesses across [CONTINENT_NAME] and beyond. With lightning-fast connectivity, low latency networking, and 24/7 uptime and reliability, our data center is equipped to handle even the most demanding workloads. Our experienced team of experts is dedicated to ensuring that your business operations run seamlessly and efficiently, making us the ideal choice for companies seeking to expand their digital capabilities.",
      "Our state-of-the-art data center, located in [LOCATION_NAME], the heart of [COUNTRY_NAME], delivers unparalleled cloud infrastructure for businesses seeking high-performance computing. With lightning-fast connectivity, low latency networking, and maximum uptime and reliability, our data center provides the ideal platform for scaling your operations across [CONTINENT_NAME] and beyond.",
      "Experience lightning-fast cloud computing with our premium infrastructure, located in [LOCATION_NAME], the vibrant hub of [COUNTRY_NAME]. Our data center boasts the latest technology and top-of-the-line hardware, ensuring maximum uptime and reliability for your business operations. Our team of experts is committed to delivering exceptional support and service, making us the trusted partner for businesses across [CONTINENT_NAME].",
      "Empower your business with our cutting-edge cloud infrastructure, located in [LOCATION_NAME], the thriving capital city of [COUNTRY_NAME]. Our data center features low-latency networking, lightning-fast connectivity, and around-the-clock support, providing the optimal platform for businesses seeking to expand their digital capabilities. Whether you're operating locally or globally, our data center is equipped to handle your most demanding workloads.",
      "Unlock the full potential of your business with our world-class cloud infrastructure, located in [LOCATION_NAME], the bustling metropolitan center of [COUNTRY_NAME]. Our data center offers maximum uptime and reliability, lightning-fast connectivity, and low-latency networking, delivering the optimal platform for businesses operating across [CONTINENT_NAME] and beyond. With our experienced team of experts, your business operations will run seamlessly and efficiently.",
      "Discover the power of high-performance cloud computing with our cutting-edge infrastructure, located in [LOCATION_NAME], the vibrant economic center of [COUNTRY_NAME]. Our data center features lightning-fast connectivity, low-latency networking, and maximum uptime and reliability, making us the trusted partner for businesses seeking to expand their digital capabilities. With our skilled team of experts, your business operations will run smoothly and efficiently, enabling you to focus on growth and success.",
    ]
  r = randint(0,len(lst)-1)
  return lst[r].replace("[LOCATION_NAME]",city).replace("[COUNTRY_NAME]",cntry).replace("[CONTINENT_NAME]",region)