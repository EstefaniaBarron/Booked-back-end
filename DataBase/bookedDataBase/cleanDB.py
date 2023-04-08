
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookedDataBase.settings")
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookedDataBase.settings')

#run this command first in terminal
#export DJANGO_SETTINGS_MODULE=bookedDataBase.settings

from django.conf import settings
from singleBookData.models import Book
from singleBookData.models import Listing

def cleanCondition():
    listingsToClean = Listing.objects.filter(condition="N/A").update(condition="Used")
    print(listingsToClean)
    listingsDirty = Listing.objects.filter(condition="N/A")
    print("conditions N/A found:",listingsDirty,"\n")


###main below
cleanCondition()