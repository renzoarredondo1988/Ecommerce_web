from django.shortcuts import render
#creo funciones con pass para configurar urls y settings
# views.py en tu aplicación
from django.shortcuts import render

def home(request):
    # procesar la lógica necesaria antes de renderizar el template
    return render(request, 'nombre_template_home.html')  # Renderiza el template para la página principal

def about(request):
    # procesar la lógica necesaria antes de renderizar el template
    return render(request, 'nombre_template_about.html')  # Renderiza el template para la página Acerca de...
