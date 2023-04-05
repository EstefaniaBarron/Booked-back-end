import os
import time
import subprocess

authorsFile = open("authors.txt",'r')
completedAuthors = open("authors_added.txt","r")
completed = list((completedAuthors.read()).split('\n'))
#print(completed)
lastUpdated = completed[-1]
completedAuthors.close()

toAdd = authorsFile.read()
toAddList = list(toAdd.split('\n'))

#find the index where we last left off on 
for i in toAddList:
    if i == lastUpdated:
        newIndex = toAddList.index(i)
        toAddList = toAddList[newIndex+1:]

authorsAdded = open("authors_added.txt","a")

command="python manage.py runscript scrape_insert --script-args "


for i in toAddList:
    name = '"'+i+'"'
    #print(name,"\n")
    commandToRun = command +name
    print(commandToRun,"\n")

    subprocess.call(commandToRun, shell=True)
    print("\n\n\ncompleted\n\n")
    authorsAdded.write(i+"\n")
    completed.append(name)


#close all files
authorsAdded.close()
authorsFile.close()