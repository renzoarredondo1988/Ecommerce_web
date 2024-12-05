from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    oculto = models.BooleanField(default=False)

    def __str__(self):
        return f"Carrito {self.id} de {self.usuario}"