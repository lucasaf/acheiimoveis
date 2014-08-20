# coding: utf-8
from django.db import models
from django.db.models import Q


class RealEstate(models.Model):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50, blank=False, null=False)
    razao_social = models.CharField('Razão Social', max_length=100, blank=False, null=False)
    cresci = models.CharField('Cresci', max_length=45, blank=False, null=False)
    cnpj = models.IntegerField('CNPJ', max_length=14, blank=False, null=False)
    numero = models.IntegerField('Número', max_length=10, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    telefone = models.IntegerField('Telefone',  max_length=10, blank=False, null=False)
    site = models.CharField('Site',  max_length=50, blank=True, null=True)
    email = models.EmailField('Email',  max_length=45, blank=False, null=False)
    logo = models.ImageField('Logo', upload_to='imobiliarias', blank=True)
    is_active = models.BooleanField('Ativo?',default=True)

    class Meta:
        verbose_name = 'Imobiliaria'
        verbose_name_plural = 'Imobiliarias'
        ordering = ['nome_fantasia']

    def __unicode__(self):
        return self.nome_fantasia


class Realtor(models.Model):
    nome = models.CharField('Nome Fantasia', max_length=45, blank=False, null=False)
    cresci = models.CharField('Cresci', max_length=45, blank=False, null=False)
    cpf = models.IntegerField('CPF', max_length=11, blank=False, null=False)
    numero = models.IntegerField('Número', max_length=10, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    telefone = models.IntegerField('Telefone',  max_length=10, blank=False, null=False)
    celular = models.IntegerField('Celular',  max_length=11, blank=False, null=False)
    site = models.CharField('Site',  max_length=50, blank=True, null=True)
    email = models.EmailField('Email',  max_length=45, blank=False, null=False)
    foto = models.ImageField('Foto', upload_to='corretores', blank=True)
    is_active = models.BooleanField('Ativo?',default=True)

    class Meta:
        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'
        ordering = ['nome']

    def __unicode__(self):
        return self.nome
