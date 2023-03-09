from . import settings as S
from . import plugins as P
from . import shell as SHELL
from flask import render_template

def the404page(email,redirect=False):
  addHtml = ""
  if redirect:
    addHtml += "<script>window.location.href = '"+S.Urls["login"]+"'</script>"
  return render_template("dashboard.html",data = {
      "Settings":S,
      "pluginLinks":P.getAllHomeLinks(email),
      "pluginHTML":"<h1>404</h1>"+addHtml,
      "pageTitle":" | "+ "404",
      })


def theDashboardHomePage(email,name,dp):
  return render_template("dashboard.html",data = {
      "Settings":S,
      "name": "Anonymous" if name=="" else name,
      "pluginLinks":P.getAllHomeLinks(email),
      "display_picture":dp,
      "pluginHTML":'''
        <div class="w3-container">
          <h1>Welcome To The O2</h1>

           <div class="w3-card-4">
              <header class="w3-container w3-pink">
                <h1>ifconfig</h1>
              </header>
              <div class="w3-container">
                <pre>'''+SHELL.execute(SHELL.cmdStringToList("ifconfig"))+'''</pre>
              </div>
            </div> 
          


        </div>
      ''',
      "pageTitle": "Home",
      })
