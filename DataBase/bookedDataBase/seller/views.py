from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

#from ...api import AddressSerializer
from api.serializers import SellerSerializer

from .models import bookSellerSite
from .models import Address


class SellersView(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = bookSellerSite.objects.all()
