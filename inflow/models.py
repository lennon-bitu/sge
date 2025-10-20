from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Inflow(models.Model):
    suplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows', verbose_name='Fornecedor')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows', verbose_name='Produto')
    quantity = models.IntegerField(verbose_name='Quantidade')
    desceription = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.product.title} - {self.quantity} unidades'
