from django.db import models

class Store(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=100, null=False)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=20, unique=True)
    date_of_fundation = models.DateTimeField(auto_now=True)
