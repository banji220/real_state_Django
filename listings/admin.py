from django.contrib import admin
from .models import Listing

class AdminListing(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "price", "list_date", "realtor")
    list_display_links = ("id", "title")
    list_filter = ("realtor", "price")
    
admin.site.register(Listing, AdminListing)