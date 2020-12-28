from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "price", "list_date",)

admin.site.register(Listing, ListingAdmin)