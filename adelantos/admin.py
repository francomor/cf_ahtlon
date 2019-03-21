from django.contrib import admin

from .models import Adelanto

# Register your models here.
class AdelantoAdmin(admin.ModelAdmin):
    #actions = [reporte_actividades]
    fields = ("cliente", "actividad", "forma_pago", "monto")
    search_fields = ['cliente__nombre']
    list_display = ["cliente", "get_actividades", "fecha", "monto"]

    def get_actividades(self, obj):
    	return " | ".join([act.nombre for act in obj.actividad.all()])

    get_actividades.short_description = "Actividades"

admin.site.register(Adelanto, AdelantoAdmin)
