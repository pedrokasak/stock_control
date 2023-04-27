from django.shortcuts import render, redirect

from store.forms import StoreForm
from store.models import Store


def store(request):
    templates_html = 'store.html'
    stores = Store.objects.all()
    return render(request, templates_html, {'store': store})


def create_store(request):
    templates_html = 'create_store.html'
    form = StoreForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('store:store')
        else:
            print(form.errors)

    return render(request, templates_html, {'form': form})


def edit_store(request, pk):
    stores = Store.objects.get(pk=pk)
    form = StoreForm(request.POST or None, instance=stores)
    if form.is_valid():
        form.save()
        return redirect('store:store')
    else:
        print(form.errors)
        return render(request, 'edit_store.html', {'form': form})


def delete_store(request, pk):
    stores = Store.objects.get(pk=pk)
    if request.method == 'POST':
        stores.delete()
        return redirect('store:store')
    return render(request, 'delete_store.html', {'stores': stores})

