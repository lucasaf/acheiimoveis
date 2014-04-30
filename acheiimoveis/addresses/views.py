# coding: utf-8
from django.views.generic import base
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Q, District, City, State
from .forms import DistrictForm, CityForm, StateForm


class DistrictList(base.View):
    label = 'Bairros'
    template_name = 'districts/district_list.html'

    def get(self, request):
        pass
