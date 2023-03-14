name = "MOUS_azureManager"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "mouse-field"
privLevel = 9  # This is a plugin ID ... to be used as a refference
publicLinks = ["main", "mresult"]

from funcs import settings as S


def main(request):
  return template("")


def mresult(request):
  x = int(request.form.get("n1")) * int(request.form.get("n2"))
  ans = "<h1> Result: " + str(x) + "</h1>"
  return template(ans)


def template(result):
  return '''
  <div class="w3-container">
    <h1><img src="https://icons8.com/icon/vqF20UXnIgtz/rat" style="width:100%;"> Azure Manager</h1>
    <form method="post" action="''' + S.Urls["plugin"].replace(
    '<name>', name).replace("<functionCall>", "mresult") + '''">
      <input name="n1" type="number">
      <input name="n2" type="number">
      <input type="submit">
    </form>
    ''' + str(result) + '''
  </div>
  '''
