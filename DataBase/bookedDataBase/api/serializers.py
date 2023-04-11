

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


class ListingsSerializer(serializers.ListSerializer):
    def to_representation(self, instance):
        # OMG please rewrite this in the near future, lest the Gods of CompSci seek revenge
        req_condition = self.context['request'].GET.get('condition')
        req_min_price = self.context['request'].GET.get('price_min')
        req_max_price = self.context['request'].GET.get('price_max')
        if req_condition and req_max_price and req_min_price:
            instance = instance.filter(
                condition=req_condition, price__lte=req_max_price, price__gte=req_min_price)
            # return super(ListingsSerializer, self).to_representation(instance)
        if req_condition and req_min_price and not req_max_price:
            instance = instance.filter(
                condition=req_condition, price__gte=req_min_price)
        if req_condition and req_max_price and not req_min_price:
            instance = instance.filter(
                condition=req_condition, price__lte=req_max_price)
        if req_condition and req_min_price and not req_max_price:
            instance = instance.filter(
                condition=req_condition, price__gte=req_min_price)
        if req_max_price and req_min_price and not req_condition:
            instance = instance.filter(
                price__lte=req_max_price, price__gte=req_min_price)
        if req_max_price and req_condition and not req_min_price:
            instance = instance.filter(
                condition=req_condition, price__lte=req_max_price)
        if req_min_price and not req_max_price and not req_condition:
            instance = instance.filter(price__gte=req_min_price)
        if req_max_price and not req_condition and not req_min_price:
            instance = instance.filter(price__lte=req_max_price)
        if req_condition and not req_min_price and not req_max_price:
            instance = instance.filter(condition=req_condition)

        return super(ListingsSerializer, self).to_representation(instance)


class ListingsListSerializer(serializers.ModelSerializer):
    # Add name of store in view, as opposed to id
    book_store = serializers.CharField(source='book_store.StoreName')
    #isbn = serializers.CharField(source='isbn.title')

    class Meta:
        model = Listing
        list_serializer_class = ListingsSerializer
        fields = ('book_store', 'price', 'condition', 'link_url')


class BookSerializer(serializers.ModelSerializer):
    availability = ListingsListSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'binding', 'availability')
