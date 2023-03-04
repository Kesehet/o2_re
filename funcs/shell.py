import subprocess
import json 
from funcs import settings as S








def cmdStringToList(str:str):
    return str.split(" ")

def pre():
    pass

def run(s:str):
    return execute(cmdStringToList(s))

def execute(cmdList:list):
    try:
        return subprocess.check_output(cmdList).decode('ascii')
    except subprocess.CalledProcessError as e:
        return e.output.decode("ascii")

def getAllCommands(index:int,params:dict):
    return setCommandParams(params,commands[index]["cmd"])

def setCommandParams(params:dict,cmd:str):
    preFix = "<[*"
    postFix = "*]>"
    keys = list(params.keys())
    vals = list(params.values())
    for i in range(len(keys)):
        cmd = cmd.replace(preFix+keys[i]+postFix,vals[i])
    return cmd

# commands = []
# cmd = "curl -sS -X GET "+S.CouchDBLogin+"/cmds/_all_docs"
# cmds = str(run(cmd))
# userMeta = json.loads(cmds)
# for user in userMeta["rows"]:
#     commands.append(json.loads(run(
#     "curl -sS -X GET " + S.CouchDBLogin + "/cmds/"+user["id"]
#     )))
# #print(commands)
