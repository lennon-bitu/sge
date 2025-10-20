from django.db import models
from brands.models import Brand
from categories.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', null=True, blank=True, verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', null=True, blank=True, verbose_name='Categoria')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    serial_number = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='Número de Série')
    ean = models.CharField(max_length=13, unique=True, null=True, blank=True, verbose_name='EAN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, verbose_name='Preço de Custo')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Venda')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['title']

    def __str__(self):
        return self.title