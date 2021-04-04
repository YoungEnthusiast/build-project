from django.contrib import admin
from .models import ProductCustomer, ProductWalletHistorie
from django.contrib.auth.models import User

class ProductCustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
    search_fields = ['user__username', 'phone_Number', 'state', 'city', 'address']
    list_filter = ['city', 'state']

    list_display_links = ['user', 'CAC_Certificate']
    list_per_page = 10

admin.site.register(ProductCustomer, ProductCustomerAdmin)

class ProductWalletHistorieAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount_debited', 'amount_credited', 'current_balance', 'date_recorded']
    search_fields = ['user__username', 'amount_debited', 'amount_credited', 'current']
    list_filter = ['amount_debited', 'amount_credited']
    list_display_links = ['user']
    list_per_page = 10

admin.site.register(ProductWalletHistorie, ProductWalletHistorieAdmin)
