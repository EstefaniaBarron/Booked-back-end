from django.urls import include, path
from rest_framework import routers
from seller.views import SellersView
from singleBookData.views import BooksView
from singleBookData.views import ListingListView

router = routers.DefaultRouter()
router.register(r'sellers', SellersView)
router.register(r'books', BooksView)
router.register(r'listings', ListingListView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
