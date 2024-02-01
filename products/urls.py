from django.urls import path

from products.views import products, create_product, edit_product, delete_products

app_name = 'products'

urlpatterns = [
    path('list-products/', products, name='products'),
    path('create-product/', create_product, name='create_product'),
    path('edit-product/<int:pk>', edit_product, name='edit_product'),
    path('delete-product/<int:pk>', delete_products, name='delete_products'),
]
