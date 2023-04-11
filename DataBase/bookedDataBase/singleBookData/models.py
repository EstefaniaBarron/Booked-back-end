from django.db import models
from seller.models import bookSellerSite


class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=5000)
    binding = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000)


class Listing(models.Model):
    book_store = models.ForeignKey(
        bookSellerSite, related_name='available_at', on_delete=models.CASCADE)
    link_url = models.URLField(max_length=5000)
    condition = models.CharField(max_length=100)
    price = models.FloatField(max_length=300)
    #price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.ForeignKey(
        Book, related_name="availability", on_delete=models.CASCADE)
