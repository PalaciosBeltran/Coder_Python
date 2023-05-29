from django.contrib import admin
from . import models

@admin.register(models.DestinoCategoria)
class DestinoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "departamento", "descripcion", "foto")
