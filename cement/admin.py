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
    list_display = ['id', 'user', 'customer', 'cement', 'quantity', 'payment_mode', 'total_price', 'schedule_delivery', 'order_status', 'payment_status', 'address', 'city', 'state', 'date_ordered', 'last_modified']
    search_fields = ['id', 'user', 'customer', 'cement', 'quantity', 'payment_mode', 'date_ordered', 'last_modified', 'order_status', 'payment_status']
    list_filter = ['cement', 'payment_mode', 'order_status', 'payment_status', 'checkout']
    list_display_links = ['id', 'user', 'customer', 'cement']
    list_per_page = 10

admin.site.register(CementOrder, CementOrderAdmin)

class GuestCementOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'state', 'city', 'address', 'cement', 'quantity', 'payment_mode', 'total_price', 'schedule_delivery', 'order_status', 'payment_status', 'date_ordered']
    search_fields = ['id', 'name', 'email', 'state', 'city', 'address', 'cement', 'quantity', 'payment_mode', 'total_price', 'date_ordered', 'order_status', 'payment_status']
    list_filter = ['state', 'city', 'cement', 'payment_mode', 'order_status', 'payment_status']
    list_display_links = ['id', 'name', 'email', 'cement']
    list_per_page = 10

admin.site.register(GuestCementOrder, GuestCementOrderAdmin)

class CustomerWalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence', 'date_Submitted']
    search_fields = ['user', 'amount_Paid', 'transaction_Date', 'transaction_Name']
    list_filter = ['transaction_Date', 'transaction_Name']
    list_display_links = ['user', 'payment_Evidence']
    list_per_page = 10

admin.site.register(CustomerWallet, CustomerWalletAdmin)
