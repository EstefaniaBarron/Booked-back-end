# Booked-back-end

Back-end for Booked prototype. Team Gold, CS 411W.
The contents of this README will be focused on:

- Project installation
- Usage of scraping functionality
- Accessing of database
- REST API usage

## Project Installation

_Assuming this repository has been successfully cloned_
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

## Rest API

There are currently two end points in the Rest API:

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
