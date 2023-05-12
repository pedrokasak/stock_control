from django.db import models


class Customers(models.Model):
    name = models.CharField(verbose_name='Cliente', max_length=150, null=False, blank=False)
    cpf = models.CharField(verbose_name='CPF', max_length=16, null=False, blank=False, unique=True)
    date_of_birth = models.DateField(auto_now=False)
    service = models.CharField(verbose_name='Serviço', max_length=100, null=True, blank=True)
    create_by = models.DateTimeField(auto_now_add=True)
    address = models.CharField(verbose_name='Rua', max_length=100, null=True)
    city = models.CharField(verbose_name='Cidade', max_length=100, null=True)
    state = models.CharField(verbose_name='Estado', max_length=20, null=True)
    country = models.CharField(verbose_name='País', max_length=50, null=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.name
