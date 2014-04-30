# coding: utf-8
from django import forms
from .models import District, City, State


class DistrictForm(form.ModelForm):

    class Meta:
        model = District


class CityForm(form.ModelForm):

    class Meta:
        model = City


class StateForm(form.ModelForm):

    class Meta:
        model = State
