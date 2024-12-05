from django.db import models

from carrito.models import Carrito;

# Create your models here.
class Pasarela(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=45, null=True)
    total = models.FloatField(null=True)
    fecha = models.DateTimeField(null=True)

    def __str__(self):
        return f"Pasarela {self.id} - Estado: {self.estado}"