from django import forms
from .models import UserOrder, VisitorOrder, OrderStatus
from django.forms.widgets import NumberInput
from django.core.exceptions import ValidationError
import datetime

class UserOrderForm(forms.ModelForm):
    PAYMENT_CHOICES=[('Pay Instantly','Pay Instantly'),
         ('Pay on Site', 'Pay on Site')]
    payment_Mode = forms.ChoiceField(label='Payment Mode', choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
    DELIVERY_CHOICES=[('Normal (Single)', 'Normal (Single)'),
         ('Joined (To be delivered with orders in the same area)', 'Joined (To be delivered with orders in the same area)')]
    delivery_Type = forms.ChoiceField(label='Delivery Type', choices=DELIVERY_CHOICES, widget=forms.RadioSelect)
    schedule_Delivery = forms.DateField(label='Schedule Delivery', widget=NumberInput(attrs={'type': 'date'}))
    email = forms.EmailField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered email address'}),
                          required = False)
    phone_Number = forms.CharField(label='Phone Number', widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered phone number'}),
                          required = False)
    city= forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered city'}),
                          required = False)
    address = forms.CharField(widget= forms.TextInput
                          (attrs={'placeholder':'Leave blank if you wish to use registered address'}),
                          required = False)

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if state == "Select a State":
            raise ValidationError("Please select a state from the dropdown")
        return state

    def clean_schedule_Delivery(self):
       schedule_Delivery = self.cleaned_data.get('schedule_Delivery')
       if schedule_Delivery < datetime.date.today() + datetime.timedelta(days=2):
           raise ValidationError("You cannot schedule within less than 48 hours")
       return schedule_Delivery

    class Meta:
        model = UserOrder
        fields = ['email', 'phone_Number', 'state', 'city', 'address', 'payment_Mode',  'delivery_Type', 'schedule_Delivery']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].help_text = "Select from the available states we have for now"

class VisitorOrderForm(forms.ModelForm):
    PAYMENT_CHOICES=[('Pay Instantly','Pay Instantly'),
         ('Pay on Site', 'Pay on Site')]
    payment_Mode = forms.ChoiceField(label='Payment Mode', choices=PAYMENT_CHOICES, widget=forms.RadioSelect)
    DELIVERY_CHOICES=[('Normal (Single)', 'Normal (Single)'),
         ('Joined (To be delivered with orders in the same area)', 'Joined (To be delivered with orders in the same area)')]
    delivery_Type = forms.ChoiceField(label='Delivery Type', choices=DELIVERY_CHOICES, widget=forms.RadioSelect)
    schedule_Delivery = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if state == "Select a State":
            raise ValidationError("Please select a state from the dropdown")
        return state

    def clean_schedule_Delivery(self):
        schedule_Delivery = self.cleaned_data.get('schedule_Delivery')
        if schedule_Delivery < datetime.date.today() + datetime.timedelta(days=2):
            raise ValidationError("You cannot schedule within less than 48 hours")
        return schedule_Delivery

    class Meta:
        model = VisitorOrder
        fields = ['first_Name', 'last_Name', 'email', 'phone_Number', 'state', 'city', 'address', 'payment_Mode',  'delivery_Type', 'schedule_Delivery']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].help_text = "Select from the available states we have for now"

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ['order', 'order_Status']
