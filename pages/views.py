from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_choices, state_choices, price_choices
from realtors.models import Realtor
def home(request):
    listings = Listing.objects.order_by("list_date").filter(is_published=True)[:3]
    context = {
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
    }
    return render(request, "pages/home.html", context)

def about(request):
    # Get All Realtor
    realtors = Realtor.objects.order_by("-hire_date")
    # Get MVP Realtor
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    
    
    context = {
        "realtors": realtors,
        "mvp_realtor": mvp_realtor
    }
    return render(request, "pages/about.html", context)