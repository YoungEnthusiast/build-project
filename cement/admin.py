from django.contrib import admin

from .models import *

class CementAdmin(admin.ModelAdmin):
    list_display = ['type', 'price', 'date']
    search_fields = ['type', 'price', 'date']
    list_filter = ['type']

    list_display_links = ['type']
    list_per_page = 10

admin.site.register(Cement, CementAdmin)

class CementOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cement', 'quantity', 'total_price', 'date_ordered', 'last_modified', 'status']
    search_fields = ['id', 'user', 'cement', 'quantity', 'date_ordered', 'last_modified', 'status']
    list_filter = ['cement', 'status']
    list_display_links = ['id', 'user', 'cement',]
    list_per_page = 10

admin.site.register(CementOrder, CementOrderAdmin)

class GuestCementOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'state', 'cement', 'quantity', 'total_price', 'date_ordered', 'status']
    search_fields = ['id', 'name', 'address', 'city', 'state', 'cement', 'quantity', 'total_price', 'date_ordered', 'status']
    list_filter = ['city', 'state', 'cement', 'status']
    list_display_links = ['id', 'name', 'cement',]
    list_per_page = 10

admin.site.register(GuestCementOrder, GuestCementOrderAdmin)
