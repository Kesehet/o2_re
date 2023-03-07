from . import settings as S
from . import logger as Log
from . import users as U
from . import shell as SHELL
import json
from cryptography.fernet import Fernet
from urllib.parse import urlencode


Log.writeLog("Database","Update",S.databaseType +" is being used." )





def getUsers():
  userMeta = getTable("users")
  ret = []
  for user in userMeta["rows"]:
    ret.append(json.loads(SHELL.execute(SHELL.cmdStringToList(
      "curl -sS -X GET " + S.CouchDBLogin + "/users/"+user["id"] 
    ))))
  return ret



def getUserByName(name:str):
  cmd = "curl -X GET -u 'admin:6Jr9Z8L#k5F!@yxBM7%$S&KPcAfX3G2d' db.3duverse.com/users/_design/docs/_view/by_name?key=\""+urlencode(name)+"\""
  rows = json.loads(SHELL.execute(SHELL.cmdStringToList(cmd)))["rows"]
  return getRowFromTable(rows["id"],"users")

def getRowFromTable(rowID,Table):
   rowID = urlencode(rowID)
   Table = urlencode(Table)
   return json.loads(SHELL.execute(SHELL.cmdStringToList(
      "curl -sS -X GET " + S.CouchDBLogin + "/"+Table+"/"+rowID 
    )))

def getTable(tableName:str):
   cmd = "curl -sS -X GET "+S.CouchDBLogin+"/"+tableName+"/_all_docs"
   return json.loads(SHELL.execute(SHELL.cmdStringToList(cmd)))

#______________________TEMP FUNCTIONS___________________________
def createTable(tableName):
   tableName = str(urlencode(tableName)).lower()
   cmd = "curl -u 'admin:6Jr9Z8L#k5F!@yxBM7%$S&KPcAfX3G2d' -X PUT "+S.CouchDBLogin+"/"+tableName
   Log.writeLog("Database","Update","Table Creation Log \n"+SHELL.run(cmd))






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



createTable("users")
createTable("tasks")
