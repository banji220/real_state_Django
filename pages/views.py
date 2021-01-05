from django.shortcuts import render
from listings.models import Listing

def home(request):
    
    return render(request, "pages/home.html")
def about(request):
    return render(request, "pages/about.html")