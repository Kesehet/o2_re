import shell as SHELL



IP = '0.0.0.0'
PORT = 80

Urls = {
  "base":"https://control.3duverse.com",
  "dashboard":"/dashy",
  "login":"/login",
  "google_login_check":"/google_is_really_cool",
  "google_logout_check":"/bye_bye_google",
  "db":"/api/<name>/<functionCall>",
  "plugin":"/myPlugins/<name>/<functionCall>",
  "edgeCertify":"/3duverse.com.pem",
  "edgeKey":"/3duverse.com.key"
  }




databaseType = "couchdb" #"000webhost" #"mongodb"

gClientId = "342128468133-amah5bt2bcgk2stcio4p0423923alnnt.apps.googleusercontent.com"

encryptionKey = "iu6pxcSjuDt7TuGx_Y-iHQqp6h-9tlbh_b-cXKDuJUM=" #os.environ['encryption_key']

invalidUserMessage = "You really shouldn't be here !"


favicon = "https://purelifi.com/wp-content/uploads/2018/10/O2-logo.png"


CouchDBLogin = "admin:6Jr9Z8L%23k5F!%40yxBM7%25%24S%26KPcAfX3G2d@db.3duverse.com"






from threading import Timer, Thread

def call_at_interval(time, callback, args):
    while True:
        timer = Timer(time, callback, args=args)
        timer.start()
        timer.join()

def setInterval(time, callback, *args):
    Thread(target=call_at_interval, args=(time, callback, args)).start()


cmds = [
    "git checkout main",
    "git pull",
    "git merge origin/main"
]

def asyncFunction(cmds:list):
    for cmd in cmds:
      SHELL.run(cmd)


setInterval(10, asyncFunction, cmds)
