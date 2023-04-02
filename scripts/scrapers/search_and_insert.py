#from the_strand import scrape_the_strand
from prince_bookstore import scrape_prince_books
from second_and_charles import scrape_2nd_and_charles

import os

import json
import sys


def find(book):
    scrape_prince_books(book, True)
    #scrape_2nd_and_charles(book, True)


find(sys.argv[1])
