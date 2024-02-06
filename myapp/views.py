from django.shortcuts import render
from django.http import HttpResponse
from .models import ShagufTask
from .utils import fetch_and_insert_data  
 #Create your views here.
def index(request):
    # Fetch data from Google Sheets and insert into the database
    fetch_and_insert_data()

   #Success message in browser
    return HttpResponse("Data synchronization complete.")
#
