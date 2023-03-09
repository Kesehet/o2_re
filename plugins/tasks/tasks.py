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

  return template(str(resp))




def template(result):

  boxes = ""
  for b in result:
    boxes = boxes + box(b["name"],[
      "<b>Name:</b>"+b["status"]["name"],
      "<b>Name:</b>"+b["status"]["description"]
    ])

  return '''
  <div class="w3-container">
		<h2>Task List</h2>
		<div class="w3-row">
			<div class="w3-col s12 m6 l4">
				<div class="w3-card">
					<div class="w3-container w3-grey">
						<h3>Finish project report</h3>
					</div>
					<div class="w3-container">
						<p><b>Due Date:</b> March 15, 2023</p>
						<p><b>Status:</b> Not started</p>
					</div>
				</div>
			</div>

			<div class="w3-col s12 m6 l4">
				<div class="w3-card">
					<div class="w3-container w3-blue">
						<h3>Call mom</h3>
					</div>
					<div class="w3-container">
						<p><b>Due Date:</b> March 12, 2023</p>
						<p><b>Status:</b> Complete</p>
					</div>
				</div>
			</div>
		</div>
	</div>
  '''
def box(name:str,properties:list):
  lst = ""
  for prop in properties:
    lst = lst + "<p>"+prop+"</p>"
  return '''
      <div class="w3-col s12 m6 l4">
				<div class="w3-card">
					<div class="w3-container w3-green">
						<h3>''' + name + '''</h3>
					</div>
					<div class="w3-container">
						''' + lst + '''
					</div>
				</div>
			</div>
      '''