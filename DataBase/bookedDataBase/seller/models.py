from django.db import models

# Create your models here.
class bookSellerSite(models.Model):
    StoreName =models.CharField(max_length =5000)
    Address = models.CharField(max_length=5000)
    StoreSite =models.URLField(max_length=5000)