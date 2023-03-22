from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

#from ...api import AddressSerializer
#from api.serializers import SellerSerializer
from api.serializers import BookSerializer

#from .models import bookSellerSite
#from .models import Address
from .models import Listing
from .models import Book


class BooksView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
