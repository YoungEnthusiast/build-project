from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import ProductCustomer, ProductWalletHistorie
from django.core.exceptions import ValidationError

class CustomRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)

    def clean_email(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
           raise ValidationError("A user with the supplied email already exists")
       return email

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if User.objects.filter(username=username).exists():
           raise ValidationError("A user with the supplied username already exists")
       return username

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].help_text = "This field is required. It must be a valid email address"
        self.fields['username'].help_text = "This field is required. It can contain letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"

class ProfileEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        #self.fields['email'].label = "Email Address"


class ProductCustomerEditForm(forms.ModelForm):
    CAC_Certificate = forms.ImageField(required = False)

    def clean_state(self):
       state = self.cleaned_data.get('state')
       if state == "Select a State":
           raise ValidationError("Please select a state from the dropdown")
       return state

    class Meta:
        model = ProductCustomer
        fields = ['phone_Number', 'state', 'city', 'address', 'CAC_Certificate']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['CAC_Certificate'].help_text = "This field is only mandatory for QwikXplorers"
        self.fields['CAC_Certificate'].label = "CAC Certificate"
class AdminCreditForm(forms.ModelForm):
    class Meta:
        model = ProductWalletHistorie
        fields = ['user', 'amount_credited']
