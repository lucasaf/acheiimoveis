# coding: utf-8
from django.db import models
from django.db.models import Q


class Property(models.Model):
    descricao = models.CharField('Descricão', max_length=500, blank=False, null=False)
    referencia = models.CharField('Referência', max_length=45, blank=False, null=False)
    numero = models.IntegerField('Número', max_length=10, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    estagio = models.CharField('Estagio',  max_length=45, blank=False, null=False)
    dormitorio = models.IntegerField('Dormitório',  max_length=2, blank=False, null=False)
    is_active = models.BooleanField('Ativo?',default=True)

    class Meta:
        verbose_name = 'Propiedade'
        verbose_name_plural = 'Propiedades'
        ordereing = ['descricao']

    def __unicode__(self):
        return self.descricao


class Image(models.Model):
    caminho_imagem = models.ImageField('imagem', upload_to='imoveis', blank=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordereing = ['caminho_imagem']

    def __unicode__(self):
        return self.caminho_imagem


class characteristic(models.Model):
    tipo = models.Charfield('Tipo', max_length=45, blank=False, null=False)
    descricao = models.Charfield('Descrição', max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Caracteristicas'
        ordereing = ['tipo']

    def __unicode__(self):
        return self.tipo
