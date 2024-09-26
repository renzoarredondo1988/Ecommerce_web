from django.urls import path
from InterfazGeneral import views
urlpatterns = [
    path('', views.home, name='home'),  # URL para la página principal
    path('about/', views.about, name='about'),  # URL para la página Acerca de
]