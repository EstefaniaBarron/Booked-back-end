from singleBookData.models import Book
from singleBookData.models import Listing
from seller.models import bookSellerSite
import csv
#from scripts.prince_bookstore import scrape_prince_books
from scripts.second_and_charles import scrape_2nd_and_charles
#from models import Listing


'''
Function to store data into database if scrape_prince_books's store_in_db argument is True

'''


def run(*args):

    #prince_books_data = scrape_prince_books(args[0])
    # create_items(prince_books_data)
    second_charles_data = scrape_2nd_and_charles(args[0])
    create_items(second_charles_data)


def create_items(data):
    for item in data:
        file_binding = item["binding"]
        file_title = item["title"]
        file_author = item["author"]
        file_price = item["price"]
        file_isbn = item["isbn"]
        file_url = item["url"]
        file_store = item["store"]
        file_condition = item["condition"]

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
