name = "MOUS_azureManager"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "mouse-field"
privLevel = 3  # This is a plugin ID ... to be used as a refference
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
    <h1 class="w3-tooltip">
      <img src="https://icons8.com/icon/vqF20UXnIgtz/rat" style="width:100%;"> 
      Azure Manager
    </h1>
    <div class="w3-text w3-tiny">
      Yes, as an Azure Cloud Manager, I am capable of managing all your machines in Azure including creating, deleting, and load balancing them using Azure PowerShell. Additionally, I can provide you with analytics on all the machines to help you make informed decisions about your infrastructure.

      Here are some of the tasks I can perform for you using Azure PowerShell:

      Create virtual machines: I can use Azure PowerShell to create virtual machines for you in Azure.

      Delete virtual machines: If you want to delete virtual machines, I can use Azure PowerShell to do it for you.

      Load balancing: I can configure load balancing for your virtual machines using Azure PowerShell. This will ensure that your applications remain available even if one or more virtual machines fail.

      Monitor machines: I can use Azure PowerShell to monitor the performance of your virtual machines, including CPU usage, memory usage, and disk space.

      Analytics: I can provide you with detailed analytics on your virtual machines, including usage patterns, performance trends, and resource consumption. This information can help you optimize your infrastructure and reduce costs.

      Overall, as your Azure cloud manager, I will ensure that your infrastructure runs smoothly, and I will provide you with the insights you need to make informed decisions about your infrastructure.
    </div>
    ''' + str(result) + '''
  </div>
  '''
