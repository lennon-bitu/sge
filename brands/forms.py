from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  ', 'placeholder': 'Nome da Marca'}),
            'description': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500', 'placeholder': 'Descrição'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        }