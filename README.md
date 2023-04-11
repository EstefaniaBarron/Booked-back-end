# Booked-back-end

Back-end for Booked prototype. Team Gold, CS 411W.
The contents of this README will be focused on:

- Project installation
- Usage of scraping functionality
- Accessing of database
- REST API usage

## Project Installation

_Assuming this repository has been successfully cloned,_

To run the contents of this repository:

- Install all dependencies
  - Inside the main directory, navigate to **DataBase/bookedDataBase**:
    - `cd DataBase/bookedDataBase`
  - In this directory, there are two requirements files. One is for pip environments, and one for conda. Both _should_ work.
    - To install pip environment:
    ```
    python3 -m venv env
    source env/bin/activate
    pip install -r pip_requirements.txt
    ```
    - To install conda environment:
    ```
    conda create --name <env> --file conda_requirements.txt
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
5. Click on any of the endpoints to see data:
   ![Alt text](../../../Desktop/Screen%20Shot%202023-04-11%20at%201.32.03%20PM.png)

### **/books** ###:

Returns all books in database in JSON format

### **/sellers** ###:

Returns a list of all sellers that had a useful site in Hampton Roads, and their locations

## scripts/scrapers folder

### **the_strand.py**:

File scrapes through inventory of The Strand bookstore searching for input title, and outputs a file containing a list of listings. Each listing is in the following format: {title, author, price, binding, link}
**Updates:** Not being used in find.py, since The Strand is out of the Hampton Rds area :(

    Usage: to use, provide a string title for the search
    Example: python the_strand.py "Love in the Time of Cholera"

### **prince_bookstore.py**:

Script scrapes through inventory of Prince Bookstore (Norfolk, VA), searches for input string, and returns details of books currently available in-store.

    Usage: Called on by find.py

### **second_and_charles.py**:

Script scrapes through inventory of 2nd and Charles website, searches for input string, and returns details of books available in-store.

    Usage: Called on by find.py

**Considerations:** 2nd and Charles website does not specify which of the store's location each listing is available at.

### **find.py**:

Consolidation of all scraper scripts.

    Usage: python3 find.py "input"
    *where input is a book title, author, isbn, or keyword

**Details:** find.py calls on each one of the scraper scripts sending the 'input' string as an argument.

**Output:** Script will add a file to the search_outputs folder with the name 'input_search_output.txt', where 'input' is the input string used in the search.

    Output file will be in the form "[{listing},{listing},{listing}...]
    where each listing is an object in the form:
        {
         binding: "Hardcover" or "Paperback",
         title: title of book,
         author: name of the author,
         price: price, in $ amount,
         isbn: isbn of book,
         url: url of book details with buying options,
         store: store where the listing came from
         condition: condition listed on the seller's website
         }

### Hampton Roads Bookshops:

Dog Eared Books: Inventory not available online

Barnes and Noble

The Way We Were: No Website available

Bender's Books and Cards: No Website available

Prince Books

Paperbacks Ink: Inventory not available online

Book Owl: No Website available

Jeannie's Used Books: No Website available

afk Books and Records: No Website available

2nd and Charles

Book Exchange: Inventory not available online

Eleanor's Norfolk: Inventory not available online

# Populate DJANGO ORM Database commands:

use the automation script, automationFill.py path: .../Booked-back-end/DataBase/bookedDataBase/automationFill.py

# Server update

after the automation script runs,run python manage.py makemigrations to update the database
