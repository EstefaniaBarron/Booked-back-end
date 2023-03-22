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
        fields = ('book_store', 'link_url', 'price', 'isbn')


class BookSerializer(serializers.ModelSerializer):
    available_at = ListingsSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'binding', 'available_at')
