from django.shortcuts import render, redirect
from suppliers.forms import SupplierForm
from suppliers.models import Suppliers


def suppliers(request):
    template_name = 'suppliers.html'
    suppliers = Suppliers.objects.all()
    context = {'suppliers': suppliers}
    return render(request, template_name=template_name, context=context)


def create_supplier(request):
    template_name = 'create_supplier.html'
    form = SupplierForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('suppliers:suppliers')
        else:
            print(form.errors)
    return render(request, template_name=template_name, context=context)


def edit_supplier(request, pk):
    supplier = Suppliers.objects.get(pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    template_name = 'edit_supplier.html'
    if form.is_valid():
        form.save()
        return redirect('customers:customers')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, template_name=template_name, context=context)


def delete_supplier(request, pk):
    supplier = Suppliers.objects.get(pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers:delete_supplier')
    return render(request, 'delete_supplier.html', {'supplier': supplier})
