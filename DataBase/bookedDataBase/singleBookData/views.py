from django.shortcuts import render
from rest_framework import viewsets
import django_filters.rest_framework as filters
from api.serializers import BookSerializer
from api.serializers import ListingsSerializer
from api.serializers import ListingsListSerializer
from .models import Listing
from .models import Book

# Filters through Books model.
# Overwriting filterset class behavior to return books that contain title and author string vs exact match


class BooksFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    condition = filters.CharFilter(
        field_name='availability__condition', lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'binding', 'author', 'condition']


class ListingsFilter(filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            'price': ['lte', 'gte'],
            'condition': ['iexact']
        }


class BooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    serializer_class = BookSerializer
    filterset_class = BooksFilter


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingsSerializer


class ListingListView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingsListSerializer
    filterset_class = ListingsFilter
