from django.urls import path

from .views import StoreView

urlpatterns = [
    path('store', StoreView.as_view(), name='store')
]