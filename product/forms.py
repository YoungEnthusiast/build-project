from django import forms
from .models import ProductOrder, GuestProductOrder, CustomerCredit
#from django.core import validators
#from django.forms.widgets import SelectDateWidget
from django.forms.widgets import NumberInput

class ProductOrderForm(forms.ModelForm):
    #schedule_delivery = forms.DateField(widget=SelectDateWidget, required = False)
    schedule_delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered email address'}),
                          required = False)
    phone_number = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered phone number'}),
                          required = False)
    address = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered address'}),
                          required = False)
    city= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered city'}),
                          required = False)
    state= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank to use registered state'}),
                          required = False)
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity', 'payment_mode', 'schedule_delivery', 'email', 'phone_number', 'state', 'city', 'address']
        labels = {
            'payment_mode': 'Payment Mode', 'schedule_delivery': 'Schedule Delivery'
        }

class CustomerCreditForm(forms.ModelForm):
    transaction_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)
    class Meta:
        model = CustomerCredit
        fields = ['amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence']


class GuestProductOrderForm(forms.ModelForm):
    schedule_delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = GuestProductOrder
        fields = ['name', 'email', 'phone_number', 'state', 'city', 'address', 'product', 'quantity', 'payment_mode', 'schedule_delivery']
        labels = {
            'payment_mode': 'Payment Mode', 'schedule_delivery': 'Schedule Delivery'
        }
