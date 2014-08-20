# conding: utf-8
from django.shortcuts import render
from django.views.generic import base
from django.http import HttpResponseRedirect
from .models import Q, Address
from .forms import AddressForm


class AddressList(base.View):

