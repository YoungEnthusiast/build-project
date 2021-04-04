from django import forms
from .models import XploreCustomer

class XploreCustomerForm(forms.ModelForm):
    #CAC_Certificate = forms.ImageField(required = False)
    class Meta:
        model = XploreCustomer
        fields = ['phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
