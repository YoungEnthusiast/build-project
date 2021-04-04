from django import forms
from .models import ProductCredit, UserOrder, VisitorOrder
from django.forms.widgets import NumberInput

class UserOrderForm(forms.ModelForm):
    schedule_Delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered email address'}),
                          required = False)
    phone_Number = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered phone number'}),
                          required = False)
    city= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered city'}),
                          required = False)
    address = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered address'}),
                          required = False)

    class Meta:
        model = UserOrder
        fields = ['product', 'quantity', 'payment_Mode', 'schedule_Delivery', 'email', 'phone_Number', 'state', 'city', 'address']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].help_text = "Don't select if you wish to use registered state"

class ProductCreditForm(forms.ModelForm):
    transaction_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = False)
    class Meta:
        model = ProductCredit
        fields = ['amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence']


class VisitorOrderForm(forms.ModelForm):
    schedule_Delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = VisitorOrder
        fields = ['name', 'email', 'phone_Number', 'state', 'city', 'address', 'product', 'quantity', 'payment_Mode', 'schedule_Delivery']
