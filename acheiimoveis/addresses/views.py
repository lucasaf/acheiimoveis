# conding: utf-8
from django.shortcuts import render
from django.views.generic import base
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Q, Address
from .forms import AddressForm


@login_required
def address_list(request):
    address = _addres_queryset(request)

    return render(request, 'core/address_list.html', locals())


@login_required
def part_new(request):
    if request.method == 'POST':
        return part_create(request)

    form = PartForm()
    return render(request, 'core/part_form.html', locals())


def part_create(request):
    form = PartForm(request.POST, request.FILES)

    if form.is_valid():
        part = form.save(commit=False)
        part.user = request.user
        part.save()

        return HttpResponseRedirect('/pecas/')

    return render(request, 'core/part_form.html', locals())


@login_required
def part_edit(request, pk):
    part = Part.objects.get(pk=pk)

    if request.method == 'POST':
        return part_update(request, part)

    form = PartForm(instance=part)
    return render(request, 'core/part_form.html', locals())


def part_update(request, part):
    form = PartForm(request.POST, request.FILES, instance=part)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect('/pecas/')

    return render(request, 'core/part_form.html', locals())


def _part_queryset(request):
    q = request.GET.get('q')

    if not q:
        return Part.objects.all()
    else:
        return Part.objects.filter((Q(description__icontains=q) |
                                   Q(reference__icontains=q)))
