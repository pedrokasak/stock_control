from django.shortcuts import render, redirect
from customers.forms import CustomerForm
from customers.models import Customers


def customers(request):
    template_name = 'customers.html'
    customer = Customers.objects.all()
    context = {'customer': customer}
    return render(request, template_name=template_name, context=context)


def create_customer(request):
    template_name = 'create_customer.html'
    form = CustomerForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customers:customer')
        else:
            print(form.errors)
    return render(request, template_name=template_name, context=context)


def edit_customer(request, pk):
    customer = Customers.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    template_name = 'edit_customer.html'
    if form.is_valid():
        form.save()
        return redirect('customers:customers')
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, template_name=template_name, context=context)


def delete_customer(request, pk):
    customer = Customers.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer')
    return render(request, 'delete_customer.html', {'stores': customer})