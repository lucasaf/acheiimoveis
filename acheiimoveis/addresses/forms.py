# coding: utf-8
from django import forms
from .models import District, City, State


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District


class CityForm(forms.ModelForm):

    class Meta:
        model = City


class StateForm(forms.ModelForm):

    class Meta:
        model = State
