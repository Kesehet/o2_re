from cryptography.fernet import Fernet
from . import logger as Log
from google.oauth2 import id_token
from google.auth.transport import requests
from . import settings as S
def checkGoogleLoginToken(token):
  try:
    # Specify the CLIENT_ID of the app that accesses the backend:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), S.gClientId)

    # Or, if multiple clients access the backend server:
    # idinfo = id_token.verify_oauth2_token(token, requests.Request())
    # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
    #     raise ValueError('Could not verify audience.')

    # If auth request is from a G Suite domain:
    # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
    #     raise ValueError('Wrong hosted domain.')

    # ID token is valid. Get the user's Google Account ID from the decoded token.
    # userid = idinfo['sub']
    Log.writeLog("Login","Update",idinfo["name"]+" "+idinfo["email"]+" Logged in with response \n"+idinfo )
    return [1,idinfo["email"],idinfo["name"],idinfo["picture"],idinfo["sub"]]
  except Exception as e:
    Log.writeLog("Login", "Warning","Invalid Login attempt with token "+ str(token)+" "+str(e))
    return [0,"",""]
    pass



def getMyIdentifier(request):
  token = str(decrypt(request.cookies.get("userID")))
  return checkGoogleLoginToken(token)[4]


def isLoggedIn(request):
  token = str(decrypt(request.cookies.get("userID")))
  return checkGoogleLoginToken(token)
  
def LogOut(request):
  token = decrypt(request.cookies.get("userID"))
  Log.writeLog("Login","Update","user '"+checkGoogleLoginToken(token)[1]+"' logged out.")


def encrypt(text):
  if text == "":
    return ""
  try:
    key = S.encryptionKey
    fernet = Fernet(key)
    return fernet.encrypt(text.encode())
  except:
    return ""


def decrypt(text):
  if text == "":
    return ""
  try:
    text = bytes(text,'utf-8')
    key = S.encryptionKey
    fernet = Fernet(key)
    return fernet.decrypt(text).decode()
  except:
    return ""



#print(Fernet.generate_key())