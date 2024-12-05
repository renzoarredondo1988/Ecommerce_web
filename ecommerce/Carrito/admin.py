from django.contrib import admin

# Register your models here.
from .models import Carrito# Importa los modelos que deseas registrar

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Carrito)
