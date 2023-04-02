from rest_framework import serializers
from seller.models import bookSellerSite
from seller.models import Address
from singleBookData.models import Book
from singleBookData.models import Listing


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_lines', 'city', 'state', 'phone_number', 'zip_code')


class SellerSerializer(serializers.ModelSerializer):

    locations = AddressSerializer(many=True)

    class Meta:
        model = bookSellerSite
        fields = ('StoreName', 'StoreSite', 'locations')


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('book_store', 'link_url', 'price')


class ListingsListSerializer(serializers.ModelSerializer):
    # Add name of store in view, as opposed to id
    book_store = serializers.CharField(source='book_store.StoreName')
    #isbn = serializers.CharField(source='isbn.title')

    class Meta:
        model = Listing
        fields = ('book_store', 'price', 'condition', 'link_url')


class BookSerializer(serializers.ModelSerializer):
    availability = ListingsListSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'binding', 'availability')
