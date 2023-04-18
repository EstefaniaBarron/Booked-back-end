import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.headless = True
options.page_load_strategy = 'none'
options.add_argument('--no-sandbox')
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)
"""Second and Charles Bookstore Scraper
This script searches for a given string in the Second and Charles Bookstore inventory website, scrapes through the results and returns the details of all listings

The file contains the following functions:
    * scrape_2nd_and_charles - Uses selenium to search for given book and retrieves all results
    * get_details - Retrieves details about a single listing from search results
    * get_item - Retrieves inner HTML from given xpath


"""


def scrape_2nd_and_charles(book):
    """This functions scrapes through 2nd and Charle's website for the parameter string and returns the deatails of all returned listings

    Args:
        book (str): A string represented the search term to be used in website
                    Ex. Book title, author, ISBN, etc. 


    Returns:
            data (list<obj>): A list of objects containg details of each listing retrieve from search
                            Objects are in the form :
                            {
                                binding,
                                title,
                                author,
                                price,
                                isbn,
                                url,
                                store,
                                condition
                            }
    """
    data = []
    url = "https://www.2ndandcharles.com/books/browse/keyword/" + \
        book.replace(" ", "%20")

    driver.get(url)
    time.sleep(30)

    listings = driver.find_elements(By.CSS_SELECTOR, "div.product-inner")

    for listing in listings:
        try:
            data.append(get_details(listing))
        except TimeoutException:
            continue

    return data


def get_details(listing):
    """This function scrapes through an individual listing and retrieves the inner data

    Args:
        listing (selenium element): An individual listing from the search results

    Returns:
        book_details (dict): A dictionary containg the attributes and values of a single search resu;t
                                Dictionary is in the form:
                                {
                                    binding,
                                    title,
                                    author,
                                    price,
                                    isbn,
                                    url,
                                    store,
                                    condition
                                }
    """
    book_details = {
        "binding": "N/A",
        "title": "",
        "author": "",
        "price": "",
        "isbn": "",
        "url": "",
        "store": "Second and Charles",
        "condition": "N/A"
    }

    link = listing.find_element(
        By.CLASS_NAME, "product-link").get_attribute("href")
    driver_two = Chrome(options=options, service=chrome_service)
    driver_two.implicitly_wait(5)
    driver_two.get(link)
    # Wait for summary to be rendered
    summary = WebDriverWait(driver_two, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.summary')))
    # Obj is contains the xpath of each element
    obj = {
        "title": "//div[@class='summary']/h1",
        "author": "//a[@class='pdp-by-text']",
        "price": "//span[@id='salePrice']/span",
        "isbn": "//p[contains(text(),'ISBN')]"
    }
    # For each key, call get_items with to retrieve attribute from given XPATH
    for attr, path in obj.items():
        obj[attr] = get_item(path, driver_two)

    book_details['title'] = obj['title'].lstrip()
    book_details['author'] = obj['author'][obj['author'].index(
        'By ')+len('By '):] if obj['author'] != "N/A" else obj['author']
    book_details['price'] = obj['price'][1:]
    book_details['isbn'] = obj['isbn'][obj['isbn'].index(
        'ISBN # ')+len('ISBN # '):] if obj['isbn'] != "N/A"else 0
    book_details['url'] = link

    return book_details


def get_item(xpath, driver_two):
    """Helper function to retrieve title, author, price and isbn of listing given an XPATH

    Args:
        xpath (str): The XPATH to a wanted value
        driver_two (Selenium Webdriver): Initiated Web driver

    Returns:
        str: Returns a string value or N/A is the webdriver times out or if no element exists at given Xpath
    """
    try:
        val = WebDriverWait(driver_two, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))).get_attribute("innerHTML")
    except TimeoutException:
        val = "N/A"
    except NoSuchElementException:
        val = "N/A"
    return val
