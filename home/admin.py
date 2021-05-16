from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_Number', 'message', 'date_Submitted', 'status']
    search_fields = ['name', 'email' 'phone_Number', 'date_Submitted', 'status']
    list_filter = ['status']
    # list_editable = ['message']

    list_display_links = ['name', 'email']
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)
