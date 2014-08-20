# coding: utf-8
from django.db import models
from django.db.models import Q


class Address(models.Model):
    cep = models.IntegerField('CEP', max_length=8, blank=False, null=False)
    rua = models.CharField('Logradouro', max_length=100, blank=False, null=False)
    numero = models.IntegerField('Número', max_length=10, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100, blank=False, null=False)
    cidade = models.CharField('Cidade', max_length=100, blank=False, null=False)
    estado = models.CharField('Estado', max_length=100, blank=False, null=False)
    is_active = models.BooleanField('Ativo?',default=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['rua']

    def __unicode__(self):
        return self.rua +' - '+ self.numero +' - '+ self.cep
