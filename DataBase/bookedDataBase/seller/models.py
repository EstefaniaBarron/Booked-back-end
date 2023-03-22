from django.db import models

# Create your models here.


class bookSellerSite(models.Model):
    StoreName = models.CharField(max_length=5000)
    #Address = models.CharField(max_length=5000)
    StoreSite = models.URLField(max_length=5000)

# Adding Address model to allow for a one to many relationship between Seller and Address
# Ex: 2nd and Charles has multiple addresses, as does Barnes and Noble


class Address(models.Model):
    store_name = models.ForeignKey(
        bookSellerSite, related_name="locations", on_delete=models.CASCADE)
    address_lines = models.CharField(max_length=5000)
    city = models.CharField(max_length=5000)
    state = models.CharField(max_length=5000)
    phone_number = models.CharField(max_length=5000)
    zip_code = models.CharField(max_length=5000)
