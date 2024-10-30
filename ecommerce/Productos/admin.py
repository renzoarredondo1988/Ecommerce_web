from django.contrib import admin

from django.contrib import admin
from .models import Producto, Categoria, Juego, Detalles, Carrito, Usuario, Validacion, Tarjeta# Importa los modelos que deseas registrar

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Juego)
admin.site.register(Detalles)
admin.site.register(Carrito)
admin.site.register(Usuario)
admin.site.register(Validacion)
admin.site.register(Tarjeta)


                    