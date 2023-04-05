import os
import time
import subprocess

authorsFile = open("authors.txt",'r')
authorsAdded = open("authors_added.txt","a")
command="python manage.py runscript scrape_insert --script-args "
toAdd = authorsFile.read()
toAddList = toAdd.split('\n')
list(toAddList)
print(toAddList)
completed =[]
toAddList = toAddList[14:]


    

for i in toAddList:
    name = '"'+i+'"'
    #print(name,"\n")
    commandToRun = command +name
    print(commandToRun,"\n")

    subprocess.call(commandToRun, shell=True)
    print("\n\n\ncompleted\n\n")
    authorsAdded.write(i+"\n")
    completed.append(name)



