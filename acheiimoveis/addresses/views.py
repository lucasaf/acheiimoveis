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
        label = self.label

        districts = District.objects.all()

        return render(request, self.template_name, locals())

class DistrictCreate(base.View):
    label = 'Adicionar Bairros'
    template_name = 'districts/district_form.html'

    def get(self, request):
        label = self.label
        form = self.DistrictForm()

        return render(request, self.template_name, locals())

    def post(self, request):
        label = self.label
        form = self.DistrictForm(request.POST, request.FILES)

        if form.is_valid():
            district = form.save()

            return HttpResponseRedirect('/bairros/')

        return render(request, self.template_name, locals())
