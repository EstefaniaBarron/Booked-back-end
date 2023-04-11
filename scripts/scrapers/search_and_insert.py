#from the_strand import scrape_the_strand
from prince_bookstore import scrape_prince_books
from second_and_charles import scrape_2nd_and_charles

#import os

#import json
import sys


def run(book):
    scrape_prince_books(book, True)
    scrape_2nd_and_charles(book, True)


run(sys.argv[1])
