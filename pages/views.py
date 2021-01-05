from django.shortcuts import render
from  listings.views import listings

def home(request):
    return render(request, "pages/home.html", listings)
def about(request):
    return render(request, "pages/about.html")