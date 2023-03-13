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
  cmd = request.form.get("cmd")
  return template("<pre>"+SHELL.run(cmd)+"</pre>")


def template(result):
  return '''
  <div class="w3-container">
    <h1>Shell Runner</h1>
    <form method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <input name="cmd" type="text">
      <input type="submit">
    </form>
    ''' + result + '''
  </div>
  '''
