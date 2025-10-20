from django import forms
from .models import Outflow


class OutflowForm(forms.ModelForm):
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}),
            'quantity': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Quantidade'}),
            'description': forms.Textarea(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Descrição', 'rows': 4}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity > product.quantity:
            raise forms.ValidationError(f"A quantidade solicitada excede o estoque disponível, o estoque atual do produto {product.title} é {product.quantity}.")
        return quantity