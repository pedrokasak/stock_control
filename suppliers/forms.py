from django import forms
from suppliers.models import Suppliers


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers

        fields = ['name', 'cnpj','address', 'city', 'state', 'country']
        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome do fornecedor'}),
            'cnpj': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'País'}),
        }
