from django.urls import path

from suppliers.views import suppliers, create_supplier, edit_supplier, delete_supplier

app_name = 'suppliers'

urlpatterns = [
    path('list-suppliers/', suppliers, name='suppliers'),
    path('create-supplier/', create_supplier, name='create_supplier'),
    path('edit-supplier/<int:pk>', edit_supplier, name='edit_supplier'),
    path('delete-suppliers/<int:pk>', delete_supplier, name='delete_supplier'),
]
