from . import settings as S
from . import logger as Log
from . import users as U
from . import shell as SHELL
import json
from cryptography.fernet import Fernet
import requests
import datetime
from . import login as L

Log.writeLog("Database","Update",S.databaseType +" is being used." )


def fetch(urlExtension):
  req = requests.get(S.CouchDBLoginURL+urlExtension,auth=S.CouchDBLoginAuth)
  return str(req.json()).replace("'",'"')

def getSearch(table:str,_designVal:str,searchBy:str,query:str):
   query = urlencode(query)
   cmd = "/"+table+"/_design/"+_designVal+"/_view/"+searchBy+"?key=\""+query+"\""
   print("URL = " + cmd)
   return json.loads(fetch(cmd))["rows"]


def getUsers():
  userMeta = getTable("users")
  ret = []
  for user in userMeta["rows"]:
    if not user["id"].startswith("_design"):
      ret.append(getRowFromTable(user["id"],"users"))
  return ret


def getTasks():
  userMeta = getTable("tasks")
  ret = []
  for user in userMeta["rows"]:
    cmd = "/tasks/"+user["id"]
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
        task_list:list,
        request
        ):
     now = datetime.datetime.now()
     created_at = now.timestamp()
     updated_at = now.timestamp()
     name = urlencode(name.lower().replace(" ","-"))
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
     login_deatils = L.isLoggedIn(request)
     if login_deatils[0] == 0:
        return {}
     
     return {
        "name":name,
        "description":description,
        "data":data,
        "status":stat[status],
        "task_list":task_list,
        "created_by":login_deatils,
        "updated_at":updated_at,
        "created_at":created_at
     }
  

#______________________GET FUNCTIONS___________________________
def getUserByName(name:str):
  cmd = "/users/_design/docs/_view/by_name?key=\""+urlencode(name)+"\""
  rows = json.loads(fetch(cmd))["rows"]
  return getRowFromTable(rows["id"],"users")

def getUserByEmail(name:str):
  cmd = "/users/_design/docs/_view/by_email?key=\""+urlencode(name)+"\""
  rows = json.loads(fetch(cmd))["rows"]
  return getRowFromTable(rows["id"],"users")

def getTasksByUserEmail(email:str):
  ret = []
  tasks = getSearch("tasks","search","by_user_email",email)
  for task in tasks:
     ret.append(
          task["value"]
        )
  return ret

def getRowFromTable(rowID,Table):
   rowID = urlencode(rowID)
   Table = urlencode(Table)
   shell_response = fetch("/"+Table+"/"+rowID)
   Log.writeLog("Database","Update","Get Row from table -> "+ Table +" Response \n"+shell_response)
   return json.loads(shell_response)

def getTable(tableName:str):
   cmd = "/"+tableName+"/_all_docs"
   shell_response = fetch(cmd)
   Log.writeLog("Database","Update","Get Table Response -> "+ tableName+" \n"+shell_response + "\n"+cmd)
   return json.loads(shell_response)

#______________________SET FUNCTIONS___________________________

def setRow(table:str,data:dict):
  cmd = S.CouchDBLoginURL+"/"+table
  req = requests.post(cmd,auth=S.CouchDBLoginAuth,json=data)
  Log.writeLog("Database","Update", "Row Set on -> "+cmd + " \n With Response \n" + str(req.json()))
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








class CouchDB:
    """
    Class for performing CRUD operations on a CouchDB instance
    """
    from funcs import settings as S
    def __init__(self):
        self.host = S.CouchDBLoginURL
        self.auth = S.CouchDBLoginAuth

    def _make_url(self, *path):
        """
        Helper method to construct a URL from the provided path segments
        """
        segments = [f"{self.host}"]
        segments.extend(str(p) for p in path)
        return "/".join(segments)

    def create_database(self, name):
        """
        Creates a new database with the given name, if it does not already exist
        """
        url = self._make_url(name)
        response = requests.head(url, auth=self.auth)
        if response.status_code == 200:
            print(f"Database {name} already exists")
        elif response.status_code == 404:
            response = requests.put(url, auth=self.auth)
            response.raise_for_status()
            print(f"Database {name} created successfully")
        else:
            response.raise_for_status()

    def delete_database(self, name):
        """
        Deletes the database with the given name
        """
        url = self._make_url(name)
        response = requests.delete(url, auth=self.auth)
        response.raise_for_status()

    def get_document(self, db_name, doc_id):
        """
        Retrieves the document with the given ID from the specified database
        """
        url = self._make_url(db_name, doc_id)
        response = requests.get(url, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def create_document(self, db_name, data):
        """
        Creates a new document with the provided data in the specified database
        """
        url = self._make_url(db_name)
        response = requests.post(url, auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()

    def update_document(self, db_name, data):
        """
        Updates an existing document with the provided data in the specified database
        """
        doc_id = data["_id"]
        url = self._make_url(db_name, doc_id)
        response = requests.put(url, auth=self.auth, json=data)
        response.raise_for_status()
        return response.json()



    def delete_document(self, db_name, doc_id, rev):
        """
        Deletes the document with the given ID and revision from the specified database
        """
        url = self._make_url(db_name, doc_id)
        params = {"rev": rev}
        response = requests.delete(url, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()

    def search(self, db_name, view_name, **kwargs):
        """
        Executes a view query against the specified database and returns the results
        """
        url = self._make_url(db_name, "_design", view_name, "_view", view_name)
        response = requests.get(url, auth=self.auth, params=kwargs)
        response.raise_for_status()
        return response.json()
