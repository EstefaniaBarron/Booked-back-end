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


# NOTE: Configuration taken from tutorial, might need to change later
# start by defining the options
options = webdriver.ChromeOptions()
options.headless = True  # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
options.add_argument('--no-sandbox')
# options.add_argument("--remote-debugging-port=9222")
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)


# Receives book title
# Scrapes through search results of The Strand website
# Returns
def scrape_2nd_and_charles(book):
    data = []
    url = "https://www.2ndandcharles.com/books/browse/keyword/" + \
        book.replace(" ", "%20")

    driver.get(url)
    time.sleep(30)
    #ordered_list = driver.find_element(By.CLASS_NAME,"row col-12 col-lg-9 px-0 products product-list-grid pl-0 pl-lg-4")
    listings = driver.find_elements(By.CSS_SELECTOR, "div.product-inner")
    # print(ordered_list.attribute('innerHTML'))
    for listing in listings:
        data.append(get_details(listing))
    # print(data)
    #driver.quit()
    return data


def get_details(listing):
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

    obj = {
        "title": "//div[@class='summary']/h1",
        "author": "//a[@class='pdp-by-text']",
        "price": "//span[@id='salePrice']/span",
        "isbn": "//p[contains(text(),'ISBN')]"
    }

    for attr, path in obj.items():
        obj[attr] = get_item(path, driver_two)

    book_details['title'] = obj['title'].lstrip()
    book_details['author'] = obj['author'][obj['author'].index(
        'By ')+len('By '):] if obj['author'] != "N/A" else obj['author']
    book_details['price'] = obj['price']
    book_details['isbn'] = obj['isbn'][obj['isbn'].index(
        'ISBN # ')+len('ISBN # '):] if obj['isbn'] != "N/A"else obj['isbn']
    book_details['url'] = link
    #driver_two.quit()

    return book_details


def get_item(xpath, driver_two):
    try:
        val = WebDriverWait(driver_two, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))).get_attribute("innerHTML")
    except TimeoutException:
        val = "N/A"
    except NoSuchElementException:
        val = "N/A"
    return val
