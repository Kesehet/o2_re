name = "openvpn"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "shield-alt"
privLevel = 3 # This is a plugin ID ... to be used as a refference
publicLinks = [
  "main",
  "install",
  "uninstall"
]


from funcs import settings as S
from funcs import shell as SHELL
def main(request):
  return template("")


def template(result):
  isInstalled = True
  help = ""
  button = '''<a class="w3-button w3-red" href="uninstall"> Uninstall </a>'''
  try:
    help = SHELL.execute(SHELL.cmdStringToList("openvpn --help"))
  except Exception as e:
    isInstalled = False
    print(e)
    button = '''<a class="w3-button w3-green" href="install"> Install </a>''' 
  return '''
  <div class="w3-container">
    <h1>OpenVPN</h1>
    ''' +  button + '''
    
    
    <pre>'''+help+'''</pre>
  </div>
  '''

def install(request):
  SHELL.execute(SHELL.cmdStringToList("sudo apt update -y"))
  SHELL.execute(SHELL.cmdStringToList("sudo apt install -y openvpn"))
  try:
    SHELL.execute(SHELL.cmdStringToList("wget -P plugins/openvpn/downloads/  https://github.com/OpenVPN/easy-rsa/releases/download/v3.0.8/EasyRSA-3.0.8.tgz"))
  except:
    pass

  return '''
  <div class="w3-container">
      <h1>OpenVPN Installed</h1>

  </div>
    '''

def uninstall(request):
  SHELL.execute(SHELL.cmdStringToList("sudo apt remove -y openvpn"))
  SHELL.execute(SHELL.cmdStringToList("sudo apt autoremove -y"))
  return '''
  <div class="w3-container">
      <h1>OpenVPN Removed</h1>

  </div>
    '''

