from django.contrib import admin
from .models import Realtor

class RealtoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "hire_date")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    list_per_page = 25

admin.site.register(Realtor)