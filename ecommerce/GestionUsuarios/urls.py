#archivo creado manualmente llamamos a las funciones de viws y las replicamso en las url del proyecto raiz
from django.urls import path
from GestionUsuarios import views
urlpatterns = [
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_user, name='inicio_sesion'),
]