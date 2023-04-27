from django import forms
from .models import Store


class StoreForm(forms.ModelForm):
    class Meta:

        model = Store

        fields = ['name', 'cnpj', 'image', 'address', 'city', 'state', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class':'form-control', 'placeholder': 'Nome da Loja'}),
            'cnpj': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagem da loja'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe um endereço'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'País'}),
        }
