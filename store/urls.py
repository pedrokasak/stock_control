from django.urls import path
from .views import store, create_store, edit_store, delete_store

app_name = 'store'

urlpatterns = [
    path('list-store/', store, name='store'),
    path('create-store/', create_store, name='create_store'),
    path('edit-store/<int:pk>', edit_store, name='edit_store'),
    path('delete-store/<int:pk>', delete_store, name='delete_store'),
]
