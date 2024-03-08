from django.urls import re_path

from .views import reporte_actividades, get_clientes_x_actividad, get_deudores

urlpatterns = [
    re_path(r'^reporte_actividades/$', reporte_actividades),
    re_path(r'^get_clientes_x_actividad/$', get_clientes_x_actividad),
    re_path(r'^deudores/(?P<pk>[0-9]+)', get_deudores),

]
