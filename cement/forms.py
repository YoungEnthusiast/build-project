from django import forms
from .models import CementOrder, GuestCementOrder
from django.core import validators

class CementOrderForm(forms.ModelForm):
    class Meta:
        model = CementOrder
        fields = ['cement', 'quantity']
        # labels = {
        #     'phone_number': "Phone Number",
        # }
class GuestCementOrderForm(forms.ModelForm):
    class Meta:
        model = GuestCementOrder
        fields = ['name', 'address', 'city', 'state', 'cement', 'quantity']
