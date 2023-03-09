name = "tasks"
description = "I am a simple subtraction plugin that calculates the difference between two numbers."
fa_icon = "list"
privLevel = 1
publicLinks = ["main"]

from funcs import settings as S
from funcs import database as DB
from funcs import login as L
from funcs import logger as Log
def main(request):
  
  email = L.isLoggedIn(request)[1]
  
  resp = DB.getTasksByUserEmail(email)
  return template(str(resp))




def template(result):
  return '''
  <div class="w3-container">
    <h1>Subtractor Plugin</h1>
    ''' + result + '''
  </div>
  '''
