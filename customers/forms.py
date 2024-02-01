from django import forms
from customers.models import Customers
from datetime import datetime


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers

        fields = ['name', 'cpf', 'date_of_birth', 'service', 'address', 'city', 'state', 'country', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Nome do cliente'}),
            'cpf': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CPF'}),
            'date_of_birth': forms.TextInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data de nascimento'}),
            'service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serviço'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'País'}),
            'store': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione no nome da loja'}),
        }
