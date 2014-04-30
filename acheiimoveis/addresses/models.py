# coding: utf-8
from django.db import models
from django.db.models import Q


class District(models.Model):
    district = models.CharField(u'Bairro', max_length=100)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = u'Bairro'
        verbose_name_plural = u'Bairros'
        ordering = ['district']

    def __unicode__(self):
        return self.district


class City(models.Model):
    city = models.CharField(u'Cidade', max_length=100)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = u'Cidade'
        verbose_name_plural = u'Cidades'
        ordering = ['city']

    def __unicode__(self):
        return self.city

class State(models.Model):
    state = models.CharField(u'Estado', max_length=50)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['state']

    def __unicode__(self):
        return self.state
