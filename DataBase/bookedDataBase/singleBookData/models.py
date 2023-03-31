from django.db import models
from seller.models import bookSellerSite

# Create your models here.
# Create your models here.
# for help: https://realpython.com/django-migrations-a-primer/


class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=5000)
    binding = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000)


class Listing(models.Model):
    book_store = models.ForeignKey(
        Book, related_name='available_at', on_delete=models.CASCADE)
    link_url = models.URLField(max_length=5000)
    price = models.FloatField(max_length=300)
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
