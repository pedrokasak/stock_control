from django.db import models


class Store(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, null=False)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=20, unique=True)
    date_of_fundation = models.DateField(auto_now=True)
    email = models.EmailField(verbose_name='Email da empresa', unique=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True)
    address = models.CharField(verbose_name='Endereço', max_length=100, null=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    state = models.CharField(verbose_name='Estado', max_length=20, null=True)
    country = models.CharField(verbose_name='País', max_length=50, null=True)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.name


