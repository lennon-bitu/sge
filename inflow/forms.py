from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        model = Inflow
        fields = ['suplier', 'product', 'quantity', 'desceription']
        widgets = {
            'suplier': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}),
            'product': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}),
            'quantity': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Quantidade'}),
            'desceription': forms.Textarea(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Descrição', 'rows': 4}),
        }
        labels = {
            'suplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'desceription': 'Descrição',
        }