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
        return subprocess.check_output(cmdList,shell=True, env={}).decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")

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


