from django.urls import include, re_path

from .views import caja, get_caja, imprimir_recibo, ReciboCreate, generar_caja

urlpatterns = [
    re_path(r'^caja/', caja),
    re_path(r'^get_caja/', get_caja),

    re_path(r'^recibo/add/(?P<pk>[0-9]+)', ReciboCreate.as_view(), name='recibo-add'),
    # re_path(r'^cobro/(?P<pk>[0-9]+)', generar_recibo),

    re_path(r'^imprimir_recibo/(?P<pk>[0-9]+)', imprimir_recibo),
]
