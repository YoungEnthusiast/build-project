from django.contrib import admin
from .models import Customer, WalletHistory
from django.contrib.auth.models import User

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'city', 'address']
    search_fields = ['user', 'state', 'city', 'address']
    list_filter = ['city', 'state']

    list_display_links = ['user']
    list_per_page = 10

admin.site.register(Customer, CustomerAdmin)

class WalletHistoryAdmin(admin.ModelAdmin):
    list_display = ['customer', 'amount_debited', 'amount_paid', 'amount_credited', 'current_balance', 'date_recorded']
    search_fields = ['customer', 'amount_debited', 'amount_paid', 'amount_credited', 'current_balance']
    list_filter = ['amount_debited', 'amount_paid', 'amount_credited']
    list_display_links = ['customer']
    list_per_page = 10

admin.site.register(WalletHistory, WalletHistoryAdmin)
