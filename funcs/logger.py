''' 
Log Types
  Error
  DB Update
  Login Update
  Updates

'''

from funcs import settings as S


def writeLog(fileOrPlugin,logType,log):
  for channel in S.logChannels:
    if channel == logType:
      print(fileOrPlugin,logType+":",log)
  
