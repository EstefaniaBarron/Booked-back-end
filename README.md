# Booked-back-end

Back-end for Booked prototype. Team Gold, CS 411W.
The contents of this README will be focused on:

- Project installation
- Usage of scraping functionality
- Accessing of database
- REST API
  - Endpoints and Model Overview
  - Data Requests and Filtering
- Hampton Roads book shops

## Project Installation

_Assuming this repository has been successfully cloned,_

To run the contents of this repository:

- Install all dependencies
  - Inside the main directory, navigate to **DataBase/bookedDataBase**:
    - `cd DataBase/bookedDataBase`
  - In this directory, there is a requirements.txt document compatible with pip
    - To install dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

## Usage of Scraping Functionality

To use the webpage scraper:

1. Navigate to DataBase/bookedDataBase/ directory
2. In this directory, run the following command:
   - `python manage.py runscript scrape_insert --script-args "your_search_string"`
     **your_search_string**: String Parameter. The search criteria for the web scraping. It can be a book title, author, isbn, etc.
3. Running the above command will automatically insert items into the database if it yielded books not already there.
   - Example:
     If the database does not contain any books by Toni Morrison, the command `python3 manage.py runscript scrape_insert --script-args "Toni Morrison"` will scrape websites using the search string "Toni Morrison", check for existence of each listing in the database, insert all new books found.

**Considerations:**

- The scraper only scrapes websites for the following two vendors:
  - [Prince Books](https://www.prince-books.com/)
  - [Second and Charles](https://www.2ndandcharles.com/)
- The library used to run the scraper (Selenium) tends to take a lot of processing power. It _sometimes_ crashes Google Chrome web browser.
- All results of running the script are added to the database, not outputed anywhere.

## Accessing of Database

To access and visualize database contents:

1. Navigate to DataBase/bookedDataBase/ directory
2. Run the following command: `python manage.py runserver`
3. Open web browser of choice (the right choice is always Crome...)
4. On the browser, go to localhost: **http://127.0.0.1:8000/**
5. Click on any of the three endpoints that appear on the screen to see the data:
   ![Alt text](image.png)

## REST API Usage

### Endpoint and Data Models Overview

The REST API has four end points:

1.  **sellers/**
    Returns all the **sellers** in the database. Each **seller object** is in the form:

    {

        StoreName: (str) Name of the vendor,

        StoreSite: (url) Link to the vendor's website,

        locations: (list) List of address objects,

    }

    - Locations contains a list of **addresess** for physical store locations. The **address object** is in the following form:

    {

        address_line: (str) The street name, number, and
                        apt or suite number if applicable, of a physical location,

        city: (str) City of location,

        state: (str) Full name of state (Virginia, NOT VA),

        phone_number: (str) Store's listed phone number,

        zip_code: (str) Location's zip code.

    }

2.  **books/**

    Returns all the **books** stored in database. Each **book object** is in the follwing form:

    {

         isbn: (str) ISBN value of book,

         title: (str) Book title,

         author: (str) Book author,

         binding: (str) Two only possible values are
                 "Paperback"or "Hardcover"

         availability: (list) List of **listing objects**

    }

3.  **listings/**

    Returns all the **listings** stored in the database. Each **listing object** is in the following form:

    {

        book_store: (str) Name of bookstore where book
                    is available,

        price: (float) Dollar value of book from book_store

        condition: (str) Two only possible values are "Used"
                    or "New"

        link_url: (url) Link to the seller's book listing

    }

4.  **near-me/**

    By default, it returns all the **Book** objects in database.
    The main difference between this endpoint and the **books/** end point is that each **Listing** object also returns all list of all **Address** objects associated with it, including **Address** attribute **distance** which represents the distance between the **zip_code** sent in request and the **Address** object zip code attribute.

    {

         isbn: (str) ISBN value of book,

         title: (str) Book title,

         author: (str) Book author,

         binding: (str) Two only possible values are
                 "Paperback"or "Hardcover"

         availability: (list) List of **listing objects**

            book_seller: (obj) **Seller** object associated to **Listing**

                locations: (list) List of **Address* objects associated to specific **Seller**

    }

## Data Requests and Filtering

**NOTE:** Only GET opperations are currently supported

### Filtering book/ enpoint

The **Book** model is configured to be able to return all **Listings** associated with it, and to allow users to filter on **Listing** attributes as well.

To filter the database, send all parameters through the url in a request.
The following is a list of **allowed** parameter keys:

- **title** : String value
- **author** : String value
- **isbn** : String value
- **binding** : Only values accepted are "Hardcover" OR "Paperback"
- **condition** : Only values accepted are "Used" or "New"
- **price_max** : Float with two decimal places (25.00, instead of 25)
- **price_min** : Float with two decimal places (25.00, instead of 25)

**NOTE:** Order of parameters in request does not matter.

**NOTE:** While all these parameters are supported, they are **_NOT REQUIRED_**. None of the parameters have to be specified or given a value.

This means that the following query:

    GET http://127.0.0.1:8000/books/?author&title&isbn&binding=Hardcover&condition=&price_max=25.00&price_min

will return all **Book** objects (and their corresponding **Listing**s) that are Hardcover and have a price less than or equal to $25. The above query is equivalent to:

    GET http://127.0.0.1:8000/books/?binding=Hardcover&price_max=25.00

### Filtering near-me/ endpoint

In addition to accepting the same parameters as the **books/** endpoint, this endpoint accepts a **zip_code** parameter which is used to calculate the distance from each **Seller** **Address** to the sent **request_api**

To filter the database, send all parameters through the url in a request.
The following is a list of **allowed** parameter keys:

- **title** : String value
- **author** : String value
- **isbn** : String value
- **binding** : Only values accepted are "Hardcover" OR "Paperback"
- **condition** : Only values accepted are "Used" or "New"
- **price_max** : Float with two decimal places (25.00, instead of 25)
- **price_min** : Float with two decimal places (25.00, instead of 25)
- **zip_code** : Integer value

**NOTE:** Order of parameters in request does not matter.

**NOTE:** While all these parameters are supported, they are **_NOT REQUIRED_**. None of the parameters have to be specified or given a value.

This means that the following query:

    GET http://127.0.0.1:8000/books/?author&title&isbn&binding=Hardcover&condition=&price_max=25.00&price_min&zip_code=23508

will return all **Book** objects (and their corresponding **Listing**s) that are Hardcover and have a price less than or equal to $25, including a distance field. The above query is equivalent to:

    GET http://127.0.0.1:8000/books/?binding=Hardcover&price_max=25.00&zip_code=23508

### Hampton Roads book shops:

1.  **Dog Eared Books** : Inventory not available online

2.  **The Way We Were** : No Website available

3.  **Bender's Books and Cards** : No Website available

4.  **Prince Books**

5.  **Paperbacks Ink** : Inventory not available online

6.  **Book Owl**: No Website available

7.  **Jeannie's Used Books** : No Website available

8.  **afk Books and Records** : No Website available

9.  **2nd and Charles**

10. **Book Exchange** : Inventory not available online

11. **Eleanor's Norfolk** : Inventory not available online
