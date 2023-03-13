name = "shell_runner"
description = ""
fa_icon = "terminal"
privLevel = 1
publicLinks = ["main", "mresult","mps"]

from funcs import settings as S
from funcs import shell as SHELL

def main(request):
  return template("")


def mresult(request):
  cmd = request.form.get("cmd")
  return template("<pre>"+SHELL.run(cmd)+"</pre>")


def mps(request):
  cmd = request.form.get("cmd")
  return template("<pre>"+SHELL.run(cmd)+"</pre>")

def template(result):
  return '''
  <div class="w3-container">
  <div class="w3-container w3-red">Debug Only...</div>
    <h2>Shell Runner</h2>
    <form class="w3-container w3-half" method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <input name="cmd" type="text">
      <input type="submit">
    </form>
    <form class="w3-container w3-half" method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mps") + '''">
      <h2>Power Shell</h2>
      <input name="cmd" type="text">
      <input type="submit">
    </form>
    ''' + result + '''
  </div>
  '''
