from django.urls import path
from Carrito import views

urlpatterns = [
    path('', views.carrito, name='carrito'),  # URL para mostrar el contenido del carrito
    path('metodo1/', views.metodo_pago_1, name='metodo_pago_1'),#Metodos de pago. 
    path('metodo2/', views.metodo_pago_2, name='metodo_pago_2'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),  # URL para agregar un producto al carrito
    path('metodo_pago/', views.metodo_pago_mercadopago, name='metodo_pago'),

]