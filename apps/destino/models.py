from typing import Any
from django.db import models

class DestinoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    foto = models.URLField()

    class Meta:
        verbose_name = "categoría de destino"
        verbose_name_plural = "categorías de destinos"

    def __str__(self):
        return self.nombre
