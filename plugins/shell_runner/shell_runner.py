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
  return template("<h3>"+cmd+"</h3>"+"<pre>"+SHELL.run(cmd)+"</pre>")


def mps(request):
  cmd = request.form.get("cmd")
  cmd = "pwsh -Command " + cmd
  return template("<h3>"+cmd+"</h3>"+"<pre>"+SHELL.run(cmd)+"</pre>")




def template(result):
  return '''
  <div class="w3-container">
  <div class="w3-container w3-red">Debug Only...</div>
    
    <form class="w3-container w3-half" method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <h2>Shell Runner</h2>
      <textarea name="cmd" type="text"></textarea>
      <input type="submit">
    </form>
    <form class="w3-container w3-half" method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mps") + '''">
      <h2>Power Shell</h2>
      <textarea name="cmd" type="text"></textarea>
      <input type="submit">
    </form>

    <div class="w3-container">''' + result + '''</div>
  </div>
  '''
