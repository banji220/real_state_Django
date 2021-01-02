from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing


def listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page_number = request.GET.get("page")
    page_listing = paginator.get_page(page_number)
    context = {
        "listings": page_listing
    }
    
    
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    return render(request, "listings/listing.html")

def search(request):
    return render(request, "listings/search.html")