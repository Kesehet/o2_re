name = "subtractor"
description = "I am a simple subtraction plugin that calculates the difference between two numbers."
fa_icon = "minus"
privLevel = 1
publicLinks = ["main"]

from funcs import settings as S
from funcs import database as DB
from funcs import login as L

def main(request):
  
  
  return template(str(DB.getTasksByUserEmail(L.isLoggedIn(request)[1])))




def template(result):
  return '''
  <div class="w3-container">
    <h1>Subtractor Plugin</h1>
    ''' + result + '''
  </div>
  '''
