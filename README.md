# Booked-back-end

Back-end for Booked prototype. Team Gold, CS 411W

## scripts/scrapers folder

the_strand.py: File scrapes through inventory of The Strand bookstore searching for input title, and outputs a file containing a list of listings. Each listing is in the following format: {title, author, price, binding, link}

Usage: to use, provide a string title for the search
Example: python the_strand.py "Love in the Time of Cholera"

### To do: mysql database, scrapers to fill it, linking it to HTML
