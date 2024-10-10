from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la API
    path('api/catalogo/', views.api_mostrar_catalogo, name='api_mostrar_catalogo'),
    path('api/producto/<int:producto_id>/', views.api_detalle_producto, name='api_detalle_producto'),
    path('api/buscar/', views.api_buscar_productos, name='api_buscar_productos'),
    path('api/categorias/', views.obtener_categorias, name='api_obtener_categorias'),
    path('api/juegos/', views.api_ver_juegos, name='api_ver_juegos'),
]


"""
from django.urls import path
from . import views

urlpatterns = [
    path('api/productos/', views.api_ver_productos, name='api_ver_productos'),
    path('api/categorias/', views.api_ver_categorias, name='api_ver_categorias'),
    path('api/juegos/', views.api_ver_juegos, name='api_ver_juegos'),
]
"""