from django.urls import path
from customers.views import customers, create_customer, edit_customer, delete_customer


app_name = 'customers'

urlpatterns = [
    path('list-customers/', customers, name='customer'),
    path('create-customer/', create_customer, name='create_customer'),
    path('edit-customer/<int:pk>', edit_customer, name='edit_customer'),
    path('delete-customer/<int:pk>', delete_customer, name='delete_customer'),
]
