#from the_strand import scrape_the_strand
from prince_bookstore import scrape_prince_books
import json
import sys


def find(book):
    with open("search_outputs/"+book+"_search_output.txt", "w") as output:
        json.dump(scrape_prince_books(book), output)


find(sys.argv[1])
