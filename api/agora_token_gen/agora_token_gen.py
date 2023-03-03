name = "agora_token_gen"
description = "Agora token creation api."
fa_icon = "phone"
AccessID = 0
privLevel = AccessID
isOpenToPublic = True
publicLinks = [
  "main"
]

from agora_token_builder import RtcTokenBuilder

import time

def main(request):
  #You will have to set these up to generate a valid token...
  appId = "da53ac84983c494ca7597d70d178191a"
  appCertificate = "f359bef0b2f747249cb89b0c0adc4f3e"
  channelName = "Abhi"
  uid = int("0")
  role = int("0")
  privilegeExpiredTs = time.time()

  
  token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
  #printing the token that was generated
  print(token)
  return str({"response":token})