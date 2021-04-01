# from django.contrib import admin
# from .models import Customer#, WalletHistory
# from django.contrib.auth.models import User
#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone_number', 'state', 'city', 'address']
#     search_fields = ['user__username', 'phone_number', 'state', 'city', 'address']
#     list_filter = ['city', 'state']
#
#     list_display_links = ['user']
#     list_per_page = 10
#
# admin.site.register(Customer, CustomerAdmin)
# #
# # class WalletHistoryAdmin(admin.ModelAdmin):
# #     list_display = ['user', 'amount_debited', 'amount_credited', 'current_balance', 'date_recorded']
# #     search_fields = ['user__username', 'amount_debited', 'amount_credited', 'current']
# #     list_filter = ['amount_debited', 'amount_credited']
# #     list_display_links = ['user']
# #     list_per_page = 10
# #
# # admin.site.register(WalletHistory, WalletHistoryAdmin)
