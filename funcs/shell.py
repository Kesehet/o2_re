import subprocess
import json 
from funcs import settings as S



from ptyprocess import PtyProcessUnicode









def cmdStringToList(str:str):
    return str.split(" ")

def pre():
    pass

def run(s:str):
    return execute(cmdStringToList(s))

def execute(cmdList:list):
    p = PtyProcessUnicode.spawn(cmdList, dimensions=(24,130))
    script_output = []
    while True:
        try:
            script_output.append(p.readline().rstrip())
        except EOFError:
            break
    p.close()
    return ' '.join(script_output)
    # try:
    #     return subprocess.check_output(cmdList,shell=True,env={"Noob":"noob"}).decode('utf-8')
    # except subprocess.CalledProcessError as e:
    #    return e.output.decode("utf-8")

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


