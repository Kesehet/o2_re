import ssl
from flask import Flask, render_template, request, make_response,send_from_directory
from waitress import serve
import funcs.settings as S
import funcs.logger as Log
import funcs.login as L
import funcs.users as U
import funcs.plugins as P
import funcs.utilityTemplates as UT
import funcs.database as D
import os
import sys

'''
The main.py is the file that will run the flask server.
This will be the internet facing side.
This file will receive API reuests and process relevant responses.

On cloud it will be hosted on a private IP address.
We may have multiple instances running on different IPs to ensure traffic is distributed.
'''

PRIVATE_IP_ADDRESS = S.IP

app = Flask( # Create a flask app
	__name__,
	template_folder='templates', # Name of html file folder
	static_folder='static' )
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)





@app.route("/")
def main():
 return render_template("index.html",data = {"Settings":S})

@app.route(S.Urls["login"])
def login():
  return render_template("login.html",data = {"Settings":S})

@app.route(S.Urls["google_login_check"],methods=["POST"])
def login_check():
  token = request.form.get('credential')
  redirectStr = {
      "pre":"<script>window.location.href='",
         "post":"';</script>"
  }
  if L.checkGoogleLoginToken(token)[0]:
    if U.canAccessPlugin(L.checkGoogleLoginToken(token)[1],0):
      resp = make_response(redirectStr["pre"]+S.Urls["dashboard"]+redirectStr["post"])
      resp.set_cookie('userID', L.encrypt(token))
      print(resp)
      return resp
    else:
      return "/"
  else:
    return S.Urls["login"]

@app.route(S.Urls["google_logout_check"],methods=["POST"])
def logout_check():
  L.LogOut(request)
  resp = make_response(S.Urls["login"])
  resp.set_cookie('userID', "")
  return resp

@app.route(S.Urls["dashboard"])
def dashboard():
  login = L.isLoggedIn(request)
  if login[0]:
    print(login[2])
    return UT.theDashboardHomePage(login[1],login[2])
  else:
    return UT.the404page(login[1])


@app.route(S.Urls["db"],methods=["POST","GET"])
def databse(name,functionCall):
  # Putting everything in a big try catch
  try:
    # Getting the python plugin file
    __import__("api."+name+"."+name)
    plugin = sys.modules["api."+name+"."+name]
    attribs = {"Access":getattr(plugin,"AccessID"),"pubFuncs":getattr(plugin,"publicLinks"),"isOpenToPublic":getattr(plugin,"isOpenToPublic")}
    
    # Checking if the user requires login ?
    if attribs["isOpenToPublic"] == False:
      
      # Getting Login information from the user
      login = L.isLoggedIn(request)
      
      # Checking if the user can access the plugin
      if U.canAccessPlugin(login[1],attribs["Access"]) == 0 :
        return UT.the404page(login[1],True)
      
      if P.canAccessFunctionCall(functionCall,attribs["pubFuncs"]) == 0:
        return UT.the404page(login[1],True)

    #if user makes it this far ... we pass the request to the function and get the string response from the function
    func = getattr(plugin,functionCall)
    pluginReturnResponse = str(func(request))

    # Then we simply use template to show the response
    return render_template("api_response.html",data = {
      "response":pluginReturnResponse,
      })
  except Exception as e:
    Log.writeLog("Main","Error",e)
    return UT.the404page(login[1],True)
  
  #This condition will never happen ...
  return render_template("api_response.html",data = {"Settings":S,"response":resp})


@app.route(S.Urls["plugin"],methods=["GET","POST"])
def plugins(name,functionCall):
  try:
    __import__("plugins."+name+"."+name)
    plugin = sys.modules["plugins."+name+"."+name]
    attribs = {"privLevel":getattr(plugin,"privLevel"),"pubFuncs":getattr(plugin,"publicLinks")}
    login = L.isLoggedIn(request)
    if U.canAccessPlugin(login[1],attribs["privLevel"]) == 0 :
      return UT.the404page(login[1],True)
    if P.canAccessFunctionCall(functionCall,attribs["pubFuncs"]) == 0:
      return UT.the404page(login[1],True)
    func = getattr(plugin,functionCall)
    pluginReturnHTML = str(func(request))
    return render_template("dashboard.html",data = {
      "Settings":S,
      "pluginHTML":pluginReturnHTML,
      "pluginLinks":P.getAllHomeLinks(login[1]),
      "pageTitle": name,
      "name":login[2],
      })
  except Exception as e:
    Log.writeLog("Main","Error",e)
    return UT.the404page(login[1],True)






'''Some code to run the server ... '''

tempcont = ssl.SSLContext()
tempcont.load_default_certs()

app.run(host=PRIVATE_IP_ADDRESS,port=S.PORT,debug=True)
#serve(app,host=PRIVATE_IP_ADDRESS,port=S.PORT)