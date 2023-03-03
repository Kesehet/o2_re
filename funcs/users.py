from api.users.users import AccessID
from . import login as L
from . import database as DB
import hashlib

Users = DB.getUsers()

def getAllUsers():
  return DB.getUsers()


def canAccessPlugin(email,pluginAccessID):
  for user in getAllUsers():
    if user["email"] == email:
      for id in user["AccessIDs"]:
        if id == pluginAccessID:
          return 1
  return 0


def getUserLevelFromRequest(request):
  email = L.isLoggedIn(request)[1]
  for user in getAllUsers():
    if email == user["email"]:
      return user["level"]
  return None

def getUserFromRequest(request):
  email = L.isLoggedIn(request)[1]
  for user in getAllUsers():
    if email == user["email"]:
      user["databaseName"] = getDatabase(user["email"])
      return user
  return None


def getDatabase(s):
    # Create a hash object using the SHA-256 algorithm
    hash_object = hashlib.sha256(s.encode('utf-8'))

    # Get the hex-encoded hash value as a string
    hex_hash = hash_object.hexdigest()

    # Convert the hex string to a base 36 integer
    base36_int = int(hex_hash, 16) % (36**10)

    # Convert the base 36 integer to a base 36 string
    base36_str = base36_int_to_base36_str(base36_int)

    return base36_str

def base36_int_to_base36_str(i):
    # Convert an integer to a base 36 string
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    if i == 0:
        return chars[0]
    s = ''
    while i > 0:
        i, r = divmod(i, 36)
        s = chars[r] + s
    return s