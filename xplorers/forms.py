from django import forms
from .models import XploreCustomer, Request
from django.forms.widgets import NumberInput
#from django.core.exceptions import ValidationError
import datetime

class XploreCustomerForm(forms.ModelForm):
    #CAC_Certificate = forms.ImageField(required = False)
    class Meta:
        model = XploreCustomer
        fields = ['phone_Number', 'state', 'city', 'address', 'CAC_Certificate']

class RequestForm(forms.ModelForm):
    payment_Evidence = forms.ImageField(required = False, label='Payment Evidence')
    waiver_Code = forms.CharField(required=False, label='Waiver Code')
    class Meta:
        model = Request
        fields = ['package', 'image', 'payment_Evidence', 'waiver_Code']
