from django import forms
from .models import Store, Address


class StoreForm(forms.ModelForm):
    class Meta:

        model = Store

        fields = ['name', 'cnpj', 'image', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class':'form-control', 'placeholder': 'Nome da Loja'}),
            'cnpj': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'CNPJ'}),
            'image': forms.FileInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Foto'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

        fields = ['address', 'city', 'state', 'country']
        widgets = {
            'address': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Endereço da loja'}),
            'city': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Estado'}),
            'country': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'País'}),
        }
