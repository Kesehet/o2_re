from . import settings as S
from . import logger as Log
from . import users as U
from . import shell as SHELL
import json
from cryptography.fernet import Fernet




db = {}

Log.writeLog("Database","Update",S.databaseType +" is being used." )


def replitGet(key):
  if S.databaseType == "replit":
    Log.writeLog("Database", "Update","Fetched "+key+ " From DB")
    return db[key]
  else:
    Log.writeLog("Database","Error","Incorrect database in settings....")



def replitSet(key,value):
  if S.databaseType == "replit":
    Log.writeLog("Database","Update","Inserted value: "+value+" at key: "+key+ " From DB")
    db[key] = value
  else:
    Log.writeLog("Database","Error","Incorrect database in settings....")






def getUsers():
  cmd = "curl -sS -X GET '"+S.CouchDBLogin+"/users/_all_docs'"
  userMeta = json.loads(SHELL.execute(SHELL.cmdStringToList(cmd)))
  ret = []
  for user in userMeta["rows"]:
    ret.append(json.loads(SHELL.execute(SHELL.cmdStringToList(
      "curl -sS -X GET '" + S.CouchDBLogin + "/users/"+user["id"] + "'"
    ))))
  return ret




























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


