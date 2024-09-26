from django.urls import path
from Carrito import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),  # URL para mostrar el contenido del carrito
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),  # URL para agregar un producto al carrito
]