from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import User

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'state', 'wallet']
    search_fields = ['user', 'address', 'city', 'state', 'wallet']
    list_filter = ['city', 'state']

    list_display_links = ['user']
    list_per_page = 10

admin.site.register(Customer, CustomerAdmin)
