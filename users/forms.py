from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import ProductCustomer
from django.core.exceptions import ValidationError


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
           raise ValidationError("A user with the supplied email already exists")
       return self.cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].label = 'password1 label'
        self.fields['email'].help_text = "This field is required. It must be a valid email address"
        self.fields['username'].help_text = "This field is required. It can contain letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"

class ProfileEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class ProductCustomerEditForm(forms.ModelForm):
    CAC_Certificate = forms.ImageField(required = False)
    class Meta:
        model = ProductCustomer
        fields = ['phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CAC_Certificate'].help_text = "This field is only mandatory for QwikXplorers"
