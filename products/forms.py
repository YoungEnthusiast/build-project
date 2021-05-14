from django import forms
from .models import ProductCredit
from django.forms.widgets import NumberInput
from django.core.exceptions import ValidationError
import datetime

class ProductCreditForm(forms.ModelForm):
    transaction_Date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),
                            required = True, label='Transaction Date')
    class Meta:
        model = ProductCredit
        fields = ['amount_Paid', 'transaction_Date', 'transaction_Name', 'payment_Evidence']
