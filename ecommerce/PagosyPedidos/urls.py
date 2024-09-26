from django.urls import path
from . import views  # Asegúrate de que la importación sea correcta

urlpatterns = [
    path('pago/', views.realizar_pago, name='realizar_pago'),  # URL para realizar el pago
    path('pedido/', views.gestionar_pedido, name='gestionar_pedido'),  # URL para gestionar pedidos
    
]
