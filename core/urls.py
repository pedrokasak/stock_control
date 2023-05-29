from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dashboard/', include('pages.urls')),
    path('dashboard/store/', include('store.urls')),
    path('dashboard/customer/', include('customers.urls')),
    path('api/v1/', include('api.urls'))
]

urlpatterns += staticfiles_urlpatterns()

