from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('pages.urls')),
    path('dashboard/store/', include('store.urls')),
    path('dashboard/customer/', include('customers.urls'))
]

urlpatterns += staticfiles_urlpatterns()

