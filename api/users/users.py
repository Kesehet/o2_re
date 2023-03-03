name = "users"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "plus"
AccessID = 0
privLevel = AccessID
isOpenToPublic = False
publicLinks = [
  "main",
  "mresult"
]



from funcs import settings as S
from funcs import users as U



def main(request):
  return template("")

def mresult(request):
  x = int(request.form.get("n1")) + int(request.form.get("n2"))
  if x > 100 and U.getUserLevelFromRequest(request) < 1:
    ans = "<h1> You Dont have enough privilege to run this task.</h1>"
  else:
    ans = "<h1> Result: "+str(x)+"</h1>"
  return template(ans)

def template(result):
  return '''
  <div class="w3-container">
    <h1>Adder Plugin</h1>
    <form method="post" action="'''+S.Urls["plugin"].replace('<name>',name).replace("<functionCall>","mresult")+'''">
      <input name="n1" type="number">
      <input name="n2" type="number">
      <input type="submit">
    </form>
    '''+str(result)+'''
  </div>
  '''

