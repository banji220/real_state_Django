from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices
from .models import Listing
from realtors.models import Realtor

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
        "listings": listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
    }
    
    
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        "listing": listing,
        "realtors": realtors
    }
    return render(request, "listings/listing.html", context)

def search(request):
    return render(request, "listings/search.html")