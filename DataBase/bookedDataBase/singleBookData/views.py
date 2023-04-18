

from django.shortcuts import render
from rest_framework import viewsets
import django_filters.rest_framework as filters
from api.serializers import BookSerializer
from api.serializers import ListingsSerializer
from api.serializers import ListingsListSerializer
from .models import Listing
from .models import Book
from api.serializers import BookDistanceSerializer


class BooksFilter(filters.FilterSet):

    """Filter creates filter fields for the following Book attributes:
        titile - Filter against Book.title (Contains, case insensitive)
        author - Filter against Book.author (Contains, case insensitive)
        condition - Filter against Book.availability.condition (Exact -can only be Used or New)
        price_max - Filter against Book.availability.price (Less than or equal to)
        price_min - Filter aganst Book.availability.price (Greater than or equal to)
    """

    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    condition = filters.CharFilter(
        field_name='availability__condition', lookup_expr='iexact')
    price_max = filters.NumberFilter(
        field_name='availability__price', lookup_expr='lte')
    price_min = filters.NumberFilter(
        field_name='availability__price', lookup_expr='gte')

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'binding', 'author',
                  'condition', 'price_max', 'price_min']


class ListingsFilter(filters.FilterSet):
    """Filter for the following Listing attributes:
        condition - Filter against Listing.condition (Exact -can only be Used or New)
        price - Filter against Listing.price (Greater than or equal to, Less than or equal to)
    """
    class Meta:
        model = Listing
        fields = {
            'price': ['lte', 'gte'],
            'condition': ['iexact']
        }


class BooksView(viewsets.ModelViewSet):
    """ View used in books/ endpoint
        Uses BooksFilter and BooksSerializer
    """
    queryset = Book.objects.all()

    serializer_class = BookSerializer
    filterset_class = BooksFilter


class ListingView(viewsets.ModelViewSet):
    """ Uses ListingsSerializer as Serializer
    """
    queryset = Listing.objects.all()
    serializer_class = ListingsSerializer


class ListingListView(viewsets.ModelViewSet):
    """ View used in Listings serializer
        Uses ListingListSerializer and ListingsFilter
    """

    queryset = Listing.objects.all()
    serializer_class = ListingsListSerializer
    filterset_class = ListingsFilter


class BooksDistanceView(viewsets.ModelViewSet):
    """ View used in near-me/ end point
        Uses BooksDistanceSerializer and BooksFilter
    """
    queryset = Book.objects.all()

    serializer_class = BookDistanceSerializer
    filterset_class = BooksFilter
