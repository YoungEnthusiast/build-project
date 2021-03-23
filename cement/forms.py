from django import forms
from .models import CementOrder, GuestCementOrder
from django.core import validators
#from django.forms.widgets import SelectDateWidget
from django.forms.widgets import NumberInput

class CementOrderForm(forms.ModelForm):
    #schedule_delivery = forms.DateField(widget=SelectDateWidget, required = False)
    schedule_delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)

    address = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    city= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    state= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    class Meta:
        model = CementOrder
        fields = ['cement', 'quantity', 'payment_mode', 'schedule_delivery', 'state', 'city', 'address']
        labels = {
            'payment_mode': 'Payment Mode', 'schedule_delivery': 'Schedule Delivery'
        }


class GuestCementOrderForm(forms.ModelForm):
    schedule_delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)
    class Meta:
        model = GuestCementOrder
        fields = ['name', 'email', 'state', 'city', 'address', 'cement', 'quantity', 'payment_mode', 'schedule_delivery']
        labels = {
            'payment_mode': 'Payment Mode', 'schedule_delivery': 'Schedule Delivery'
        }
