# Create your models here.
from django.db import models




class Validacion(models.Model):#heredamos para que interactuen directamente con la orm de django
    correo = models.EmailField(max_length=45, null=True)
    contraseña = models.CharField(max_length=45, null=True)

    def __str__(self):#retornamso el mailcomo cadena de texto
        return self.correo

class Tarjeta(models.Model):
    fecha = models.DateField(null=True)
    numero = models.IntegerField(null=True)
    dni = models.IntegerField(null=True)

    def __str__(self):
        return str(self.numero)

class Usuario(models.Model):
    nombre = models.CharField(max_length=45, null=True)
    pais = models.CharField(max_length=45, null=True)
    apellido = models.CharField(max_length=45, null=True)
    validacion = models.ForeignKey(Validacion, on_delete=models.SET_NULL, null=True)#con el metodo .foreignkey hacemos las relaciones
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"




