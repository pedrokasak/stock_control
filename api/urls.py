from django.urls import path

from .views import StoreView, SpecificStoreView

urlpatterns = [
    path('store', StoreView.as_view(), name='store'),
    path('store/<cnpj>', SpecificStoreView.as_view(), name='store'),
]