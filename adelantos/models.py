from __future__ import unicode_literals

from django.db import models

from movimientos.models import FormaPago
from actividades.models import Actividad
from clientes.models import Cliente

class Adelanto(models.Model):
    # egreso negativo y ingreso positivo
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    #num_recibo = models.IntegerField(unique=True)
    #forma_pago = models.ForeignKey(FormaPago)
    #actividad = models.ManyToManyField(Actividad)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s | Fecha: %s | Monto: $%s" % (self.cliente, self.fecha.strftime("%Y-%m-%d"), self.monto)
