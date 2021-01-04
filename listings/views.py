from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing


def listings(request):
    page_listings = Listing.objects.all()
    paginator = Paginator(page_listings, 1)
    page_number = request.GET.get("page")
    listings = paginator.get_page(page_number)
    context = {
        "listings": listings
    }
    
    
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    return render(request, "listings/listing.html")

def search(request):
    return render(request, "listings/search.html")