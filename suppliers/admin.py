from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','created_at', 'updated_at',)
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10
    ordering = ('name',)
    

admin.site.register(Supplier, SupplierAdmin)

admin.site.site_header = 'SGE - Sistema de Gestão Empresarial'
admin.site.index_title = 'Painel de Controle'
admin.site.site_title = 'SGE Admin'  # This is the title that appears in the browser tab