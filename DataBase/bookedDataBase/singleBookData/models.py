from django.db import models

# Create your models here.
# Create your models here.
class book(models.Model):
    ISBN = models.IntegerField()
    Title= models.CharField(max_length=5000)
    Binding= models.CharField(max_length=5000)
    Author =models.CharField(max_length =5000)
    Price =models.FloatField(max_length=300)
    LinkUrl =models.URLField(max_length=5000)
    BookStore = models.CharField(max_length=5000)