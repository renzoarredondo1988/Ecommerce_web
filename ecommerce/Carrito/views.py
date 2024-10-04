from django.shortcuts import render

def carrito(request):
    return render(request,"Carrito/index.html")  # Aquí iría la lógica para mostrar el contenido del carrito

def agregar_al_carrito(request, producto_id):
    pass  # Aquí iría la lógica para agregar un producto al carrito
