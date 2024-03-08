# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static

from .utils import redireccionar

admin.site.site_header = 'CF Athlon'
admin.site.site_title = 'CF Athlon'
admin.site.site_url = None

urlpatterns = [
    re_path(r'^$', redireccionar),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^movimientos/', include('movimientos.urls')),
    re_path(r'^actividades/', include('actividades.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # lo necesita para funcionar en desarrollo
