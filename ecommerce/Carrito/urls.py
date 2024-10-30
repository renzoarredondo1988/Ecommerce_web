from django.urls import path
from Carrito import views

urlpatterns = [
    path('', views.carrito, name='carrito'),  # URL para mostrar el contenido del carrito
   

]