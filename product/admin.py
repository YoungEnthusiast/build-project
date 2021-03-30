from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['type', 'price', 'date']
    search_fields = ['type', 'price', 'date']
    list_filter = ['type']

    list_display_links = ['type']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'payment_mode', 'total_price', 'schedule_delivery', 'order_status', 'payment_status', 'address', 'city', 'state', 'date_ordered', 'last_modified']
    search_fields = ['id', 'user__username', 'product__type', 'quantity', 'payment_mode', 'date_ordered', 'last_modified', 'order_status', 'payment_status']
    list_filter = ['product', 'payment_mode', 'order_status', 'payment_status', 'checkout']
    list_display_links = ['id', 'user', 'product']
    list_per_page = 10

admin.site.register(ProductOrder, ProductOrderAdmin)

class GuestProductOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'state', 'city', 'address', 'product', 'quantity', 'payment_mode', 'total_price', 'schedule_delivery', 'order_status', 'payment_status', 'date_ordered']
    search_fields = ['id', 'name', 'email', 'state', 'city', 'address', 'product', 'quantity', 'payment_mode', 'total_price', 'date_ordered', 'order_status', 'payment_status']
    list_filter = ['state', 'city', 'product', 'payment_mode', 'order_status', 'payment_status']
    list_display_links = ['id', 'name', 'email', 'product']
    list_per_page = 10

admin.site.register(GuestProductOrder, GuestProductOrderAdmin)

class CustomerCreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence', 'date_Submitted']
    search_fields = ['user__username', 'amount_Paid', 'transaction_Date', 'transaction_Name']
    list_filter = ['transaction_Date', 'transaction_Name']
    list_display_links = ['user', 'payment_Evidence']
    list_per_page = 10

admin.site.register(CustomerCredit, CustomerCreditAdmin)
