
from app import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)