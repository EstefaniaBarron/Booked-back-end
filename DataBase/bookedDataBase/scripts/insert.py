from singleBookData.models import Book
from singleBookData.models import Listing
from seller.models import bookSellerSite
import csv
#from models import Listing


'''
Function to store data into database if scrape_prince_books's store_in_db argument is True

'''


def run():
    with open('scripts/colleen_hoover_search_results.csv') as file:
        reader = csv.reader(file)

        for row in reader:
            file_binding = row[0]
            file_title = row[1]
            file_author = row[2]
            file_price = row[3]
            file_isbn = row[4]
            file_url = row[5]
            file_store = row[6]
            file_condition = row[7]
            # If ISBN =0, ISBN did not exist. Don't even bother with it
            if file_isbn == 0:
                continue
            # Check if isbn already exists in the Book table
            existing_book = Book.objects.filter(isbn=file_isbn)
            if existing_book.exists():
                # Need actual item, not QuerySet, so use get method
                book_instance = Book.objects.get(isbn=file_isbn)
                existing_listing = Listing.objects.filter(link_url=file_url)
                if existing_listing.exists():
                    # Listing already exists
                    # UPDATE LISTING
                    # Not implemented yet
                    print("Listing exists")
                else:
                    # If Book exists, but Listing does not, create it
                    # NOTE: In the future, consider making method create_listing
                    store = bookSellerSite.objects.get(StoreName=file_store)
                    new_listing = Listing(book_store=store, link_url=file_url,
                                          condition=file_condition, price=file_price, isbn=book_instance)
                    new_listing.save()
                    print("Listings have been created")

            else:
                # No Book exists with isbn, create new Book
                new_book = Book(isbn=file_isbn, title=file_title,
                                binding=file_binding, author=file_author)
                new_book.save()
                store = bookSellerSite.objects.get(StoreName=file_store)
                new_listing = Listing(book_store=store, link_url=file_url,
                                      condition=file_condition, price=file_price, isbn=new_book)
                new_listing.save()
                print("all saved")

        # If yes,check for a Listings item
        # If no Listing item exists
        # Create one
        # Set Listing's book_store to the Book item
        # If Listing item exists
        # Update attributes (including book_store) of Listing
        # If no Book item exists, create one
        # Create Listing item
        # Add book_store of Listing as newly created Book item
