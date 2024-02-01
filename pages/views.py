from django.shortcuts import render

from customers.models import Customers
from products.models import Products
from store.models import Store
from suppliers.models import Suppliers


def index(request):
    template_html = 'index.html'
    stores = Store.objects.all().count()
    products = Products.objects.all().count()
    suppliers = Suppliers.objects.all().count()
    customers = Customers.objects.all().count()
    return render(request, template_html, {
        'stores': stores, 'products': products, 'suppliers': suppliers, 'customers': customers}
                  )
