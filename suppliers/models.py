from django.db import models


class Suppliers(models.Model):
    name = models.CharField(verbose_name='Cliente', max_length=150, null=False, blank=False)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=16, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    address = models.CharField(verbose_name='Endereço', max_length=100, null=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    state = models.CharField(verbose_name='Estado', max_length=20, null=True)
    country = models.CharField(verbose_name='País', max_length=50, null=True)

    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'

    def __str__(self):
        return self.name


