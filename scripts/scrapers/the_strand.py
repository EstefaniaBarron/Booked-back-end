import sys
import json
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
#from bs4 import BeautifulSoup

# NOTE: Configuration taken from tutorial, might need to change later
# start by defining the options
options = webdriver.ChromeOptions()
options.headless = True  # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)


def get_details(listing):
    link = listing.find_element(
        By.CSS_SELECTOR, "a[class='searchresults-product-link__link']").get_attribute('href')

    all_details = listing.find_elements(By.TAG_NAME, "p")
    return {
        "title": all_details[0].get_attribute('innerHTML'),
        "author": all_details[1].get_attribute('innerHTML'),
        "binding": all_details[2].get_attribute('innerHTML'),
        "price": all_details[3].get_attribute('innerHTML'),
        "link": link

    }


# Receives book title
# Scrapes through search results of The Strand website
# Returns
def scrape_the_strand(book):
    url = "https://www.strandbooks.com/search-results?page=1&" + \
        book.replace(" ", "%20")+"&searchVal=" + \
        book.replace(" ", "%20")+"&type=product"
    driver.get(url)
    time.sleep(10)
    content = driver.find_element(
        By.CSS_SELECTOR, "div[class='searchresults-products__div--grid']")
    results = content.find_elements(
        By.CSS_SELECTOR, "div[class='searchresults-product__div searchresults-product__div--grid']")
    data = []
    for listing in results:
        data.append(get_details(listing))

    with open('outputfile', 'w') as fout:
        json.dump(data, fout)
    # return data


scrape_the_strand(sys.argv[1])
