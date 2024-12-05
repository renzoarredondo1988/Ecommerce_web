from django.shortcuts import render
from productos.models import Producto 
#creo funciones con pass para configurar urls y settings
# views.py en tu aplicación

def home(request):
    # procesar la lógica necesaria antes de renderizar el template
    return render(request, 'interfaz_general/index.html')  # Renderiza el template para la página principal

def about(request):
    # procesar la lógica necesaria antes de renderizar el template
    return render(request, 'interfaz_general/nombre_template_about.html')  # Renderiza el template para la página Acerca de...

def buscar(request):
    query = request.GET.get('q', '')
    if query:
        # Filtra productos cuyo nombre contenga la consulta 'query'
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        # Muestra todos los productos si no hay consulta
        resultados = Producto.objects.all()
   # return render(request, 'resultado.html', {'results': results, 'query': query})