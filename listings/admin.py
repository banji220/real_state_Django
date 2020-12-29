from django.contrib import admin
from .models import Listing

class AdminListing(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "price", "list_date", "realtor")
admin.site.register(Listing)