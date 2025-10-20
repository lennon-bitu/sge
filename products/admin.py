from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category',
'description', 'serial_number', 'ean', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at',)
    
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    ordering = ('title',)
    

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'SGE - Sistema de Gestão Empresarial'
admin.site.index_title = 'Painel de Controle'
admin.site.site_title = 'SGE Admin'  # This is the title that appears in the browser tab