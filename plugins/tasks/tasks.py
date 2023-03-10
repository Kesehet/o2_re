name = "tasks"
description = "I am a simple subtraction plugin that calculates the difference between two numbers."
fa_icon = "list"
privLevel = 1
publicLinks = ["main"]

from funcs import settings as S
from funcs import database as DB
from funcs import login as L
from funcs import logger as Log
def main(request):
  
  email = L.isLoggedIn(request)[1]
  
  resp = DB.getTasksByUserEmail(email)

  return template(resp)




def template(result):

  boxes = ""
  for b in result:
    stat = b["status"]
    boxes = boxes + box(
      str(b["name"]) ,
      str(b["description"]),
      [
      "<b>"+stat["name"]+"</b>",
      "<span class='w3-hide-small' >:"+str(stat["description"])+"</span>"
    ],
    stat["name"].replace(" ", "-")
    )
  if len(result) == 0:
    boxes = '''
    <div class="w3-container blackText bold">
        Well, I guess it's time to retire and become a full-time couch potato.
        No more tasks left to tackle!
    </div>
    '''
  return '''
  <style>
    .zoomOnHover:hover {
      transform: scale(1.03);
    }
    .Not-Started{
      color: white;
      background-color: #EE4141;
    }
    .Not-Started-text{
      color: #EE4141;
    }
    .In-Progress{
      color: #313946;
      background-color: #fde74c;
    }
    .In-Progress-text{
      color: #fde74c;
    }
    .On-Hold{
      color: #313946;
      background-color: #f79256;
    }
    .On-Hold-text{
      color: #f79256;
    }
    .Completed{
      color : #313946;
      background-color: #26c485;
    }
    .Completed-text{
      color : #26c485;
    }
    .Cancelled{
      color: #313946;
      background-color: #A30015;
    }
    .Cancelled-text{
      color: #A30015;
    }
  </style>
  <div class="w3-container">
		<h2>Task List</h2>
		<div class="w3-row">

    '''+boxes+'''

		</div>
	</div>
  '''
def box(name:str,descr:str,properties:list,status:str):
  lst = ""
  for prop in properties:
    lst = lst + ""+prop+""

  return '''
        <div class = "w3-col s6 m12 l12 w3-round w3-padding zoomOnHover w3-hover-sepia">
          <div class="w3-container w3-card-4 w3-padding ">
              <div class="w3-col l4 m4 s12 w3-round w3-padding-large  ">
                <h3>''' + name + '''</h3>
              </div>
              <div class="w3-col l4 m4 s12 w3-round w3-padding-large '''+status+'''-text ">
                <p>'''+descr+'''</p>
              </div>
              <div class="w3-col l4 m4 s12 w3-padding-large '''+status+'''  ">
                <p>''' + lst + '''</p>
              </div>
          </div>
        </div>
      '''