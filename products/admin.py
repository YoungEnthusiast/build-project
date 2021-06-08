from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type']
    prepopulated_fields = {'slug': ('type',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'date', 'type', 'category', 'price', 'image']
    search_fields = ['type', 'price', 'date']
    list_filter = ['type', 'created', 'updated', 'category']
    list_display_links = ['type', 'image']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('type',)}
    list_per_page = 10

admin.site.register(Product, ProductAdmin)

class ProductCreditAdmin(admin.ModelAdmin):
    list_display = ['date_Submitted', 'user', 'amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence']
    search_fields = ['user__username', 'amount_Paid', 'transaction_Date', 'transaction_Name']
    list_filter = ['transaction_Date', 'transaction_Name']
    list_display_links = ['user', 'payment_Evidence']
    list_per_page = 10

admin.site.register(ProductCredit, ProductCreditAdmin)
