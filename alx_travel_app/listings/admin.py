from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('location', 'created_at')
    ordering = ('-created_at',)
