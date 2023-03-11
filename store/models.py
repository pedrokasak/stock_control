from django.db import models


class Address(models.Model):
    address = models.CharField(verbose_name='Rua', max_length=100, null=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    state = models.CharField(verbose_name='Estado', max_length=20, null=True)
    country = models.CharField(verbose_name='País', max_length=50, null=True)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'address'

    def __str__(self):
        return self.address


class Store(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100, null=False)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=20, unique=True)
    date_of_fundation = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d')
    address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.name


