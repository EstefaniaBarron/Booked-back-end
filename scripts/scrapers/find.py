#from the_strand import scrape_the_strand
from prince_bookstore import scrape_prince_books
from second_and_charles import scrape_2nd_and_charles

import os

import json
import sys

import db_automation


def find(book):
    with open("search_outputs/"+book+"_search_output.txt", "w") as output:
        json.dump(scrape_prince_books(book), output)
        json.dump(scrape_2nd_and_charles(book), output)





searchOutput =sys.argv[1]+"_search_output.txt"
local="/Users/nataliemohun/Documents/GitHub/Booked-back-end/scripts/scrapers/search_outputs/"

file = local+searchOutput
fileExist = os.path.exists(file)

if(fileExist==False):
    print("search already done\nrunning DB automation\n")
    find(sys.argv[1])
if(fileExist==True):
    print("going to db_automation\n")
    db_automation.driver(file)


