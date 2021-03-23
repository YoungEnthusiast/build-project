from django import forms
from .models import CementOrder, GuestCementOrder, CustomerWallet
#from django.core import validators
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

class CustomerWalletForm(forms.ModelForm):
    transaction_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)
    class Meta:
        model = CustomerWallet
        fields = ['amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence']


class GuestCementOrderForm(forms.ModelForm):
    schedule_delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)
    class Meta:
        model = GuestCementOrder
        fields = ['name', 'email', 'state', 'city', 'address', 'cement', 'quantity', 'payment_mode', 'schedule_delivery']
        labels = {
            'payment_mode': 'Payment Mode', 'schedule_delivery': 'Schedule Delivery'
        }
