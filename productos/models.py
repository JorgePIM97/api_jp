from django.conf import settings
from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=100)

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        null=True,
        blank=True
    )

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='productos_creados'
    )

    def __str__(self):
        return self.nombre