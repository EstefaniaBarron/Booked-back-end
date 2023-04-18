

from rest_framework import serializers
from seller.models import bookSellerSite
from seller.models import Address
from singleBookData.models import Book
from singleBookData.models import Listing
import pgeocode


class AddressDistanceSerializer(serializers.ModelSerializer):
    ''' Serializer for Addresses in near-me/ end point
        Methods:
            get_query_zip_code: Returns 'zip_code' parameter from request
            get_distance: Calculates distance between the zip_code attribute of address object and zip_code in request

    '''
    # Set distance to return value from class method get_distance
    distance = serializers.SerializerMethodField('get_distance')

    def get_query_zip_code(self):
        """Gets zip_code value from request

        Returns:
            str: value of zip_code parameter sent in request
        """
        return self.context['request'].GET.get('zip_code')

    def get_distance(self, obj):
        """ Calculates distance in miles between request zip code and object zip code

        Args:
            obj (Address)
            self

        Returns:
            int: Distance in miles from object zip code and request zip code
        """
        # Check to see if there was a zip code parameter sent in request
        if self.get_query_zip_code():
            # If request contained zip code, set request_zip equal to its value
            request_zip = self.get_query_zip_code()

            # Using pgeodistance to get approximate distance between request_zip and obj.request_zip
            dist = pgeocode.GeoDistance('us')
            # Convert from km to miles and return
            miles = dist.query_postal_code(request_zip, obj.zip_code)*0.621371

            return miles

    class Meta:
        model = Address
        # Added distance to fields. If distance was not calculated, field will be set to null
        fields = ('address_lines', 'city', 'state',
                  'phone_number', 'zip_code', 'distance')


class SellerDistanceSerializer(serializers.ModelSerializer):
    """ Serializer for bookSeller used in near-me/ endpoint
        locations field calls on AddressDistanceSerializer
    """

    locations = AddressDistanceSerializer(many=True)

    class Meta:
        model = bookSellerSite
        # Since locations is added to fields, address of bookSeller will be displayed
        fields = ('StoreName', 'StoreSite', 'locations')


class AddressSerializer(serializers.ModelSerializer):
    """ Address Serializer used in sellers/ endpoint

    """
    class Meta:
        model = Address
        fields = ('address_lines', 'city', 'state', 'phone_number', 'zip_code')


class SellerSerializer(serializers.ModelSerializer):
    """ Seleler serializer used in sellers/ endpoint
        locations is set to AddressSerializer to show the addresses of each seller
    """
    locations = AddressSerializer(many=True)

    class Meta:
        model = bookSellerSite
        fields = ('StoreName', 'StoreSite', 'locations')


class ListingsSerializer(serializers.ListSerializer):
    """ Listins serializer used in books/ AND near-me endpoints
        Methods:
            to_representation: configures the application of filters according to the parameters provided
    """

    def to_representation(self, instance):
        # OMG please rewrite this in the near future, lest the Gods of CompSci seek revenge
        req_condition = self.context['request'].GET.get('condition')
        req_min_price = self.context['request'].GET.get('price_min')
        req_max_price = self.context['request'].GET.get('price_max')

        if req_condition and req_max_price and req_min_price:
            instance = instance.filter(
                condition=req_condition, price__lte=req_max_price, price__gte=req_min_price)
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
    """ Listings serializer used in books/ endpoint
        book_store field will be the text value of the Listing's book_store's StoreName attribtue
    """
    # Add name of store in view, as opposed to id
    book_store = serializers.CharField(source='book_store.StoreName')

    class Meta:
        model = Listing
        list_serializer_class = ListingsSerializer
        fields = ('book_store', 'price', 'condition',
                  'link_url')


class ListingsDistanceSerializer(serializers.ModelSerializer):
    """ Listings serializer used in near-me/ endpoint
        Also uses ListingSerializer to apply filters to class
        book_store is set to SellerDistanceSerializer to also return the addresses and distance

    """
    book_store = SellerDistanceSerializer(read_only=True)

    class Meta:
        model = Listing
        list_serializer_class = ListingsSerializer
        fields = ('book_store', 'price', 'condition',
                  'link_url')


class BookDistanceSerializer(serializers.ModelSerializer):
    """ Book serializer for near-me/ end point
        availability is set to ListingsDistanceSerializer to return Listing address
    """
    availability = ListingsDistanceSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'binding', 'availability')


class BookSerializer(serializers.ModelSerializer):
    """ Book serializer used in book/ endpoint

    availability is set to ListingsListSerializer
    """
    availability = ListingsListSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'binding', 'availability')
