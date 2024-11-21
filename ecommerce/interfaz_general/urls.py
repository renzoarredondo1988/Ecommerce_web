from django.urls import path
from interfaz_general import views


app_name = 'interfaz_general' #Se crea namespace para poder acceder a estas URLs desde templates que no le pertenecen a la app

urlpatterns = [
    path('', views.home, name='home'),  # URL para la página principal
    path('about/', views.about, name='about'),  # URL para la página Acerca de
]