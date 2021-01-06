from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
def home(request):
    listings = Listing.objects.order_by("list_date").filter(is_published=True)[:3]
    context = {
        "listings": listings,
    }
    return render(request, "pages/home.html", context)

def about(request):
    realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "realtors": realtors,
    }
    return render(request, "pages/about.html", context)