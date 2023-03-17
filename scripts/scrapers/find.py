#from the_strand import scrape_the_strand
from prince_bookstore import scrape_prince_books
from second_and_charles import scrape_2nd_and_charles
import json
import sys


def find(book):
    with open("search_outputs/"+book+"_search_output.csv", "w") as output:
        json.dump(scrape_prince_books(book), output)
        json.dump(scrape_2nd_and_charles(book), output)


find(sys.argv[1])
