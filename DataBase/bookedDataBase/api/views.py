
from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

from .serializers import AddressSerializer
from .serializers import SellerSerializer

from ..DataBase.bookedDataBase.seller.models import bookSellerSite
from ..DataBase.bookedDataBase.seller.models import Address


class SellersView(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = bookSellerSite.objects.all()
