# Booked-back-end

Back-end for Booked prototype. Team Gold, CS 411W

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
