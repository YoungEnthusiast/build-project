from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['type', 'price', 'image', 'date']
    search_fields = ['type', 'price', 'date']
    list_filter = ['type']
    list_display_links = ['type', 'image']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ['order_Id', 'user', 'product', 'quantity', 'payment_Mode',  'schedule_Delivery', 'order_Status', 'payment_Status', 'phone_Number', 'state', 'city', 'address', 'date_Ordered']
    search_fields = ['order_Id', 'user__username', 'product__type', 'quantity', 'payment_Mode', 'date_Ordered', 'last_Modified', 'order_Status', 'payment_Status', 'phone_Number', 'state', 'city']
    list_filter = ['product', 'payment_Mode', 'order_Status', 'payment_Status', 'state', 'city']
    list_display_links = ['order_Id', 'user', 'product']
    list_per_page = 10

admin.site.register(UserOrder, UserOrderAdmin)

class VisitorOrderAdmin(admin.ModelAdmin):
    list_display = ['order_Id', 'name', 'email', 'state', 'city', 'address', 'product', 'quantity', 'payment_Mode', 'schedule_Delivery', 'order_Status', 'payment_Status', 'date_Ordered']
    search_fields = ['order_Id', 'name', 'email', 'state', 'city', 'address', 'product', 'quantity', 'payment_Mode', 'total_Price', 'date_Ordered', 'order_Status', 'state', 'city', 'payment_Status']
    list_filter = ['state', 'city', 'product', 'payment_Mode', 'order_Status', 'payment_Status', 'state', 'city']
    list_display_links = ['order_Id', 'name', 'email', 'product']
    list_per_page = 10

admin.site.register(VisitorOrder, VisitorOrderAdmin)

class ProductCreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence', 'date_Submitted']
    search_fields = ['user__username', 'amount_Paid', 'transaction_Date', 'transaction_Name']
    list_filter = ['transaction_Date', 'transaction_Name']
    list_display_links = ['user', 'payment_Evidence']
    list_per_page = 10

admin.site.register(ProductCredit, ProductCreditAdmin)
