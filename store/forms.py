from django import forms
from .models import Store


class StoreForm(forms.ModelForm):
    class Meta:

        model = Store

        fields = ['name', 'cnpj', 'email', 'image', 'address', 'city', 'state', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class':'form-control', 'placeholder': 'Nome da Loja'}),
            'cnpj': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ'}),
            'email': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'E-mail'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagem da loja'}),
            # 'customers': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um cliente'}),
            # 'suppliers': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione um fornecedor'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe um endereço'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'País'}),
        }
