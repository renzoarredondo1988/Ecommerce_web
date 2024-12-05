from django.db import models




class Juego(models.Model):
    logo = models.BinaryField(null=True, blank=True)
    plataforma = models.CharField(max_length=45, null=True)
    nombre = models.CharField(max_length=45, null=True)
    url_pagina = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    TIPO_CATEGORIA_CHOICES = [
        ('arma', 'Arma'),
        ('armadura', 'Armadura'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CATEGORIA_CHOICES, default='arma')

    def __str__(self):
        return self.tipo
    

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
    

