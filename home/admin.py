from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message', 'date_submitted', 'status']
    search_fields = ['name', 'email' 'phone_number', 'date_submitted', 'status']
    list_filter = ['status']
    # list_editable = ['message']

    list_display_links = ['name', 'email']
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)
