from django import forms
from .models import CementOrder, GuestCementOrder
from django.core import validators

class CementOrderForm(forms.ModelForm):
    time = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Schedule a delivery time'}),
                          required = False)
    address = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered address'}),
                          required = False)
    city= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    state= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    class Meta:
        model = CementOrder
        fields = ['cement', 'quantity', 'time', 'address', 'city', 'state']

class GuestCementOrderForm(forms.ModelForm):
    time = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Schedule a delivery time'}),
                          required = False)
    class Meta:
        model = GuestCementOrder
        fields = ['name', 'email', 'address', 'city', 'state', 'cement', 'quantity', 'time']
