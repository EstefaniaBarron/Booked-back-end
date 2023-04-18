from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

#from ...api import AddressSerializer
from api.serializers import SellerSerializer

from .models import bookSellerSite
from .models import Address


class SellersView(viewsets.ModelViewSet):
    """View Returns all objects in the Seller table

        Used in sellers/ end point
    """
    serializer_class = SellerSerializer
    queryset = bookSellerSite.objects.all()
