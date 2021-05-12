from django import forms
from django.core.exceptions import ValidationError


#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 501)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
    #                                   coerce=int)

    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    def clean_quantity(self):
        if self.cleaned_data.get('quantity') < 1:
            raise ValidationError("You cannot order less than 1")
        return self.cleaned_data.get('quantity')
