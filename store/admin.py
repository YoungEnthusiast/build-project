from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email']
    search_fields = ['user', 'name', 'email']
    list_filter = ['user']
    # list_editable = ['message']

    list_display_links = ['user', 'name', 'email']
    list_per_page = 10

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)








# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone_number', 'message', 'date_submitted', 'status']
#     search_fields = ['name', 'email' 'phone_number', 'date_submitted', 'status']
#     list_filter = ['status']
#     # list_editable = ['message']
#
#     list_display_links = ['name', 'email']
#     list_per_page = 10
#
# admin.site.register(Contact, ContactAdmin)
