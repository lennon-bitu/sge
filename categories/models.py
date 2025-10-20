from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name
