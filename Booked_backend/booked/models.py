from django.db import models

# Create your models here.
"""
    format of output file:
    title, author, binding, price, link
    for ease author name = first + last
"""
class Book(models.Model):
    title = models.CharField(max_length=2500)
    author_name= models.CharField(max_length=2500)
    binding = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    link = models.CharField(max_length=2500)