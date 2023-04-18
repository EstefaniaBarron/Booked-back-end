from django.db import models
from seller.models import bookSellerSite


class Book(models.Model):
    """ Represents a book object
        Contains isbn, title, binding, author and availability attributes
        One to many relationship to Listing
    """
    isbn = models.IntegerField()
    title = models.CharField(max_length=5000)
    binding = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000)


class Listing(models.Model):
    """ Represents a listing for a specific book from a specific store
        Contains book store name, link to listing, book condition and price.
        Connected to Book through book_store field_
    """
    # Setting related name as available_at, so attribute name of bookSellerSite will be 'available_at'
    book_store = models.ForeignKey(
        bookSellerSite, related_name='available_at', on_delete=models.CASCADE)
    link_url = models.URLField(max_length=5000)
    condition = models.CharField(max_length=100)
    price = models.FloatField(max_length=300)
    # ISBN connects Listing to Book model.
    # On Book model, attribute pointing to Listing will be called 'availability'
    isbn = models.ForeignKey(
        Book, related_name="availability", on_delete=models.CASCADE)
