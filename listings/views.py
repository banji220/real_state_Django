from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing


def listings(request):
    page_listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(page_listings, 2)
    page_number = request.GET.get("page")
    try:
        listings = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        listings = paginator.page(paginator.num_pages)
        
    context = {
        "listings": listings
    }
    
    
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    return render(request, "listings/listing.html")

def search(request):
    return render(request, "listings/search.html")