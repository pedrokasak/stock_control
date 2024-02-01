from django.db import models

from suppliers.models import Suppliers


class Products(models.Model):
    name = models.CharField(
        verbose_name='Nome do Produto', max_length=150, null=False, blank=False)
    batch = models.IntegerField(verbose_name='Lote', null=False, blank=False)
    manufacturing_date = models.DateField(auto_now=False)
    brand = models.CharField(verbose_name='Marca', max_length=50, null=True, blank=True)
    model = models.CharField(verbose_name='Modelo', max_length=50, null=True, blank=True)
    image = models.ImageField(
        verbose_name='Foto do Produto', upload_to='products/images/%m/%Y/', blank=True, null=True)
    create_by = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Suppliers, verbose_name='Fornecedores', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
