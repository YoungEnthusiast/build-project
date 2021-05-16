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
    list_display = ['xplorer', 'request_Id', 'package', 'date_Activated', 'subscription_Ends']
    search_fields = ['xplorer__user__username', 'request_Id__id', 'package', 'date_Activated', 'subscription_Ends']
    list_filter = ['package']
    list_display_links = []
    list_per_page = 10

admin.site.register(Subscription, SubscriptionAdmin)

class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'package', 'image', 'payment_Evidence', 'waiver_Code', 'created']
    search_fields = ['id', 'user__username', 'package', 'waiver_Code', 'created']
    list_filter = ['package']
    list_display_links = ['id', 'image', 'payment_Evidence']
    list_per_page = 10

admin.site.register(Request, RequestAdmin)
