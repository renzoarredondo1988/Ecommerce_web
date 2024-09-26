# En urls.py de tu aplicación Productos
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='listar_productos'),  # URL para listar productos
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # URL para el detalle del producto
]
