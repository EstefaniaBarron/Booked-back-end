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
toAddList = toAddList[1:]
print(toAddList)

for i in toAddList:
    name = '"'+i+'"'
    #print(name,"\n")
    commandToRun = command +name
    print(commandToRun,"\n")

    subprocess.call(commandToRun, shell=True)
    print("\n\n\ncompleted\n\n")
    authorsAdded.write(name+"\n")


