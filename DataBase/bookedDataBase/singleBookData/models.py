from django.db import models

# Create your models here.
# Create your models here.
class bookData(models.Model):
    ISBN = models.IntegerField()
    Author =models.CharField(max_length =5000)
    Binding= models.CharField(max_length=5000)
    Price =models.FloatField(max_length=300)
    Link =models.URLField(max_length=5000)