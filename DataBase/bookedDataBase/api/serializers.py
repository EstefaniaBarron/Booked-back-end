from rest_framework import serializers
from seller.models import bookSellerSite
from seller.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address_lines', 'city', 'state', 'phone_number', 'zip_code')


class SellerSerializer(serializers.ModelSerializer):

    locations = AddressSerializer(many=True)

    class Meta:
        model = bookSellerSite
        fields = ('StoreName', 'StoreSite', 'locations')
