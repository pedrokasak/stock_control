from django.shortcuts import render, redirect

from store.forms import StoreForm, AddressForm
from store.models import Store, Address


def store(request):
    templates_html = 'store.html'
    store = Store.objects.all()
    address = Address.objects.all()
    return render(request, templates_html, {'store': store, 'address': address})


def create_store(request):
    templates_html = 'create_store.html'
    form = StoreForm(request.POST)
    form_address = AddressForm(request.POST)
    if request.method == 'POST':
        if form.is_valid() and form_address.is_valid():
            form.save()
            form_address.save()
            return redirect('store:store')
        else:
            form = StoreForm()
            form_address = AddressForm()
    return render(request, templates_html, {'form': form, 'form_address': form_address})



