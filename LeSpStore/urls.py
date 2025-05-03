from django.contrib import admin
from django.urls import path, include
admin.site.site_header="Systarndra Fashion-Store"
admin.site.site_title ="Admin Systarndra Fashion-Store"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
