import time
import sys
import json 
from selenium.webdriver.support.ui import Select 
 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
import requests

from selenium.common.exceptions import NoSuchElementException


#NOTE: Configuration taken from tutorial, might need to change later
# start by defining the options 
options = webdriver.ChromeOptions() 
options.headless = True # it's more scalable to work in headless mode 
# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none' 
# this returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
# pass the defined options and service objects to initialize the web driver 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)


#Receives book title 
#Scrapes through search results of The Strand website
#Returns 
def scrape_prince_books(book):
    url = "https://www.prince-books.com/search/site/"+book.replace(" ","%20") 
    driver.get(url) 
    time.sleep(10)
    select= Select(driver.find_element(By.NAME,"fsort"))
    select.select_by_visible_text("In Stock")
    button = driver.find_element(By.ID, "edit-fsort-apply")
    button.submit()
    time.sleep(10)
    ordered_list = driver.find_elements(By.XPATH,"//ol[@class='search-results apachesolr_search-results']/li")
    data = []
    for listing in ordered_list:
        try:
            av = listing.find_elements(By.XPATH, "div[@class='abaproduct-details']/span")[1].text[len("Availbility: "):]

                
        except NoSuchElementException:
            av = "N/A"
        if av == ' On Our Shelves Now':
            data.append(get_details(listing))
 
    with open('outputfile.txt', 'w') as fout:
        json.dump(data, fout)       
    #return data


def get_details(listing):
    title = listing.find_element(By.XPATH,"h3[@class='title']")
    url= title.find_element(By.TAG_NAME, "a").get_attribute('href')
    all_details = extract_details(title.text)
    author = listing.find_element(By.XPATH,"div[@class='abaproduct-details']/p/a").get_attribute('innerHTML')
    all_details['author'] = author
    try:
        price = listing.find_element(By.XPATH,"div[@class='abaproduct-details']/p[@class='search-result-price']").text
    except NoSuchElementException:
        price = "N/A"
    all_details['price'] = price
    isbn = listing.find_element(By.XPATH,"div[@class='abaproduct-details']/span").text[len("ISBN-13: "):]

    all_details['isbn'] = isbn
    all_details['url'] = url

    return all_details

def extract_details(whole_string):
    obj = {}
    idx = -1
    if "(Paperback)" in whole_string:
        obj["binding"] = "Paperback"
        idx = whole_string.index("(Paperback)")
    elif "(Hardcover)" in whole_string:
        obj["binding"] = "Hardcover"
        idx = whole_string.index("(Hardcover)")
    else:
        obj["binding"] = ""
        obj["title"] = whole_string
    if idx != -1:
        title = whole_string[:idx-1]
        obj["title"] = title
    return obj
    
scrape_prince_books(sys.argv[1])