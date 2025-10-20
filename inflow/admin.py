from django.contrib import admin
from .models import Inflow


class InflowAdmin(admin.ModelAdmin):
    list_display = ('suplier', 'product', 'quantity', 'desceription', 'created_at', 'updated_at') 
    search_fields = ('product__title', 'supplier__name',)
    list_filter = ('created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    ordering = ('created_at',)
    

admin.site.register(Inflow, InflowAdmin)

admin.site.site_header = 'SGE - Sistema de Gestão Empresarial'
admin.site.index_title = 'Painel de Controle'
admin.site.site_title = 'SGE Admin'  # This is the title that appears in the browser tab