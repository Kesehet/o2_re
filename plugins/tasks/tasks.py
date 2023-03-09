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
    boxes = boxes + box(str(b["name"]),[
      "<b>Name:</b> "+stat["name"],
      "<b>Description:</b> "+str(stat["description"])
    ],
    stat["name"].replace(" " + "-")
    )

  return '''
  <style>
    .Not-Started{
      background-color: red;
    }
  </style>
  <div class="w3-container">
		<h2>Task List</h2>
		<div class="w3-row">

    '''+boxes+'''

		</div>
	</div>
  '''
def box(name:str,properties:list,status:str):
  lst = ""
  for prop in properties:
    lst = lst + "<p>"+prop+"</p>"

  return '''
      <div class="w3-col s12 m6 l4">
				<div class="w3-card">
					<div class="w3-container '''+status+''' ">
						<h3>''' + name + '''</h3>
					</div>
					<div class="w3-container">
						''' + lst + '''
					</div>
				</div>
			</div>
      '''