# coding: utf-8
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('acheiimoveis.addresses.views',
    url(r'^$', DistrictList.as_view()),
    url(r'^adicionar/$', DistrictCreate.as_view()),
)
