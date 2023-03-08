from . import settings as S
from . import logger as Log
from . import users as U
from . import shell as SHELL
import json
from cryptography.fernet import Fernet
import requests
import datetime

Log.writeLog("Database","Update",S.databaseType +" is being used." )


def fetch(urlExtension):
  req = requests.get(S.CouchDBLoginURL+urlExtension,auth=S.CouchDBLoginAuth)
  return str(req.json()).replace("'",'"')

def getUsers():
  userMeta = getTable("users")
  ret = []
  for user in userMeta["rows"]:
    cmd = "/users/"+user["id"]
    ret.append(json.loads(fetch(cmd)))
  return ret


class Schema:
  def __init__(self) -> None:
      pass
  def getTask(
        param,
        name:str,
        description:str,
        data:dict,
        status:int,
        task_list:list
        ):
     now = datetime.datetime.now()
     created_at = now.timestamp()
     updated_at = now.timestamp()
     stat = [
        {"name":"Not Started","description":" The task has been created, but work has not yet begun."},
        {"name":"In Progress","description":" Work has started on the task, but it is not yet complete."},
        {"name":"On Hold","description":" Work on the task has been temporarily paused or postponed."},
        {"name":"Dependency Blocked","description":" The task is waiting for input, approval, or completion by someone else before it can proceed."},
        {"name":"Completed","description":" The task has been finished and all necessary work has been done."},
        {"name":"Cancelled","description":" The task has been cancelled and will not be completed."},
        {"name":"Deferred","description":" The task has been delayed and will be completed at a later time."},
        {"name":"Blocked","description":" The task is currently unable to proceed due to some obstacle or issue."},
        {"name":"Urgent","description":" The task requires immediate attention and should be given priority over other tasks."},
        {"name":"High Priority","description":" The task is important and should be completed before lower priority tasks."}
     ]
     return {
        "name":name,
        "description":description,
        "data":data,
        "status":stat[status],
        "task_list":task_list,
        "updated_at":updated_at,
        "created_at":created_at
     }
  

#______________________SET FUNCTIONS___________________________
def getUserByName(name:str):
  cmd = "/users/_design/docs/_view/by_name?key=\""+urlencode(name)+"\""
  rows = json.loads(fetch(cmd))["rows"]
  return getRowFromTable(rows["id"],"users")

def getRowFromTable(rowID,Table):
   rowID = urlencode(rowID)
   Table = urlencode(Table)
   shell_response = fetch("/"+Table+"/"+rowID)
   Log.writeLog("Database","Update","Get Table "+ Table +" Response \n"+shell_response)
   return json.loads(shell_response)

def getTable(tableName:str):
   cmd = "/"+tableName+"/_all_docs"
   shell_response = fetch(cmd)
   Log.writeLog("Database","Update","Get Table Response \n"+shell_response + "\n"+cmd)
   return json.loads(shell_response)

#______________________SET FUNCTIONS___________________________

def setRow(table:str,data:dict):
  req = requests.put(S.CouchDBLoginURL+"/"+table,auth=S.CouchDBLoginAuth,json=data)
  return str(req.json()).replace("'",'"')

#______________________TEMP FUNCTIONS___________________________
def createTable(tableName):
   tableName = str(urlencode(tableName)).lower()
   cmd = "/"+tableName
   Log.writeLog("Database","Update","Table Creation Log \n"+str(fetch(cmd)) + "\n"+cmd)






# ________________________ UTILITY ______________________________

def encrypt(text):
  if text == "":
    return ""
  try:
    key = S.encryptionKey
    fernet = Fernet(key)
    return fernet.encrypt(text.encode())
  except Exception as e:
    Log.writeLog("Database","Error","Encryption Error " + str(e))
    return ""


def decrypt(text):
  if text == "":
    return ""
  try:
    text = bytes(text,'utf-8')
    key = S.encryptionKey
    fernet = Fernet(key)
    return fernet.decrypt(text).decode()
  except Exception as e:
    Log.writeLog("Database","Error","Decryption Error " + str(e))
    return ""

def toBinary(str_to_conv):
  str_to_conv = str(str_to_conv)
  return ''.join(format(ord(x), '08b') for x in str_to_conv)

def BinaryToDecimal(binary):
	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return (decimal)

def binaryToString(bin):
  str_data = ' '
  for i in range(0,len(bin),8):
    temp = int(bin[i:i+8])
    dec = BinaryToDecimal(temp)
    str_data = str_data + chr(dec)
  return str_data


URL_RFC_3986 = {
"!": "%21", "#": "%23", "$": "%24", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", 
",": "%2C", "/": "%2F", ":": "%3A", ";": "%3B", "=": "%3D", "?": "%3F", "@": "%40", "[": "%5B", "]": "%5D",
}

def urlencode(b):
    if type(b)==bytes:
        b = b.decode(encoding="utf-8") #byte can't insert many utf8 charaters
    result = bytearray() #bytearray: rw, bytes: read-only
    for i in b:
        if i in URL_RFC_3986:
            for j in URL_RFC_3986[i]:
                result.append(ord(j))
            continue
        i = bytes(i, encoding="utf-8")
        if len(i)==1:
            result.append(ord(i))
        else:
            for c in i:
                c = hex(c)[2:].upper()
                result.append(ord("%"))
                result.append(ord(c[0:1]))
                result.append(ord(c[1:2]))
    result = result.decode(encoding="ascii")
    return result











createTable("users")
createTable("tasks")


