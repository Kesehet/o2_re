name = "iptables"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "chart-area"
privLevel = 3 # This is a plugin ID ... to be used as a refference
publicLinks = [
  "main",
]


from funcs import settings as S
from funcs import shell as SHELL
def main(request):
  return template("")


def template(result):
  return '''
  <div class="w3-container">
    <h1>IPtables</h1>
    <pre>'''+SHELL.execute(SHELL.cmdStringToList("iptables -h"))+'''</pre>
  </div>
  '''

