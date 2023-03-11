name = "subtractor"
description = "I am a simple subtraction plugin that calculates the difference between two numbers."
fa_icon = "minus"
privLevel = 1
publicLinks = ["main", "mresult"]

from funcs import settings as S
from funcs import shell as SHELL
import subprocess

def main(request):
  p = subprocess.Popen(["pwsh","-Command","'Write-Host \"Hello World\"'"], stdout=subprocess.PIPE)
  p_out, p_err = p.communicate()
  print(p_out)
  return SHELL.run("")
  #return SHELL.run("pwsh -Command \"Get-AzConsumptionUsageDetail -ResourceGroup fill-masjid-com_group -StartDate 2022-12-31 -EndDate 2023-03-10\"")


def mresult(request):
  ans = "<h1> Result: " + str(
    int(request.form.get("n1")) - int(request.form.get("n2"))) + "</h1>"
  return template(ans)


def template(result):
  return '''
  <div class="w3-container">
    <h1>Subtractor Plugin</h1>
    <form method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <input name="n1" type="number">
      <input name="n2" type="number">
      <input type="submit">
    </form>
    ''' + result + '''
  </div>
  '''
