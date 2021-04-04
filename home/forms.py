from django import forms
from .models import Contact
#from django.core import validators

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_Number', 'message']
