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

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    oculto = models.BooleanField(default=False)

    def __str__(self):
        return f"Carrito {self.id} de {self.usuario}"
class Categoria(models.Model):
    TIPO_CATEGORIA_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CATEGORIA_CHOICES, default='arma')

    def __str__(self):
        return self.tipo


class Juego(models.Model):
    logo = models.BinaryField(null=True, blank=True)
    plataforma = models.CharField(max_length=45, null=True)
    nombre = models.CharField(max_length=45, null=True)
    url_pagina = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=250, null=True)
    stock = models.IntegerField(null=True)
    nombre = models.CharField(max_length=45, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen=models.ImageField(upload_to="tienda",null=True,blank=True)

    def __str__(self):
        return self.nombre

class Detalles(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=True)
    precio = models.FloatField(null=True)

    def __str__(self):
        return f"Detalle {self.id} del carrito {self.carrito}"

class Pasarela(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=45, null=True)
    total = models.FloatField(null=True)
    fecha = models.DateTimeField(null=True)

    def __str__(self):
        return f"Pasarela {self.id} - Estado: {self.estado}"
