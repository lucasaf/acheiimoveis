# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('acheiimoveis.core.views',
    url(r'^$', 'index', name='index'),
)
