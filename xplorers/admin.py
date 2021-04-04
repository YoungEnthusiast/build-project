from django.contrib import admin
from .models import XploreCustomer
from django.contrib.auth.models import User

class XploreCustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
    search_fields = ['user__username', 'phone_Number', 'state', 'city', 'address']
    list_filter = ['city', 'state']

    list_display_links = ['user', 'CAC_Certificate']
    list_per_page = 10

admin.site.register(XploreCustomer, XploreCustomerAdmin)
