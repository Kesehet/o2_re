name = "resources"
description = "A simple plugin that show resource usage of a server."
fa_icon = "flask"
privLevel = 0
publicLinks = [
  "main",
]

import psutil
import os


def main(request):
  return template("")


def template(result):
  #print(psutil.cpu_percent + " " + psutil.virtual_memory().percent)
  return '''
  <div class="w3-container">
    <h1>Resource Utilization</h1>
    <div class="w3-container w3-white">
      <h4>CPU Percent :- ''' + str(psutil.cpu_percent()) + '''%</h4>
      <h4>RAM Usage :- ''' + str(psutil.virtual_memory().percent) + '''%</h4>
      <h4>Disk Usage :- ''' + str(psutil.disk_usage(os.getcwd())) + '''</h4>
      
    </div>
  </div>
  '''
