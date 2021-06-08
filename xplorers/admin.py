from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

class XploreCustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
    search_fields = ['user__username', 'phone_Number', 'state', 'city', 'address']
    list_filter = ['city', 'state']
    list_display_links = ['user', 'CAC_Certificate']
    list_per_page = 10

admin.site.register(XploreCustomer, XploreCustomerAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['date_Activated', 'subscription_Ends', 'xplorer', 'request_Id', 'package']
    search_fields = ['date_Activated', 'subscription_Ends', 'xplorer__user__username', 'request_Id__id', 'package']
    list_filter = ['package']
    list_display_links = []
    list_per_page = 10

admin.site.register(Subscription, SubscriptionAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'user', 'package', 'image', 'payment_Evidence', 'waiver_Code']
    search_fields = ['created', 'id', 'user__username', 'package', 'waiver_Code']
    list_filter = ['package']
    list_display_links = ['id', 'image', 'payment_Evidence']
    list_per_page = 10

admin.site.register(Request, RequestAdmin)
