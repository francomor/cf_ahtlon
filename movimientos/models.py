# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from actividades.models import Actividad
from clientes.models import Cliente


class FormaPago(models.Model):
    tipo = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.tipo


class Recibo(models.Model):
    # egreso negativo y ingreso positivo
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    num_recibo = models.IntegerField(unique=True)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.DO_NOTHING)
    actividad = models.ManyToManyField(Actividad)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s | $%s | Numero de recibo: %s" % (self.cliente, self.monto, self.num_recibo)

    def str_numero_y_fecha(self):
        return "Fecha: %s | Numero de recibo: %s | Monto: $%s" % (self.fecha.strftime("%Y-%m-%d"), self.num_recibo, self.monto)


class CierreCaja(models.Model):
    fecha = models.DateField(auto_now_add=True)
    total_efectivo = models.DecimalField(max_digits=8, decimal_places=2)
    total_tarjeta = models.DecimalField(max_digits=8, decimal_places=2)
    recibo_desde = models.CharField(max_length=8, unique=True)
    recibo_hasta = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return "%s | $%d" % (self.fecha, self.total_efectivo + self.total_tarjeta)
