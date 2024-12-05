from django.contrib import admin

from .models import Producto, Categoria, Juego# Importa los modelos que deseas registrar

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Juego)



                    