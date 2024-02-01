from django import forms

from products.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:

        model = Products

        fields = ['name', 'batch', 'manufacturing_date', 'brand', 'model', 'image', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'batch': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Lote'}),
            'manufacturing_date': forms.TextInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de criação'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'modelo'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione no nome do fornecedor'}),
        }
