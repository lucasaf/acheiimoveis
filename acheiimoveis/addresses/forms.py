# conding: utf-8
from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
