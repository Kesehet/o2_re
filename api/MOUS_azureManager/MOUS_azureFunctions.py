from funcs import database as DB

def getAllTasks():
    return DB.getTasks()

def main():
    #We get all Tasks
    ret = DB.getSearch("tasks","search","all_not_started","")
    return str(ret)