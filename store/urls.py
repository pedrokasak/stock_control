from django.urls import path
from .views import store, create_store

app_name = 'store'

urlpatterns = [
    path('list-store/', store, name='store'),
    path('create-store/', create_store, name='create_store')
]
