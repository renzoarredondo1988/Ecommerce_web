from django.shortcuts import render
from GestionUsuarios.models import Producto, Categoria, Juego, Detalles
from django.db.models import Subquery, OuterRef  
from django.http import JsonResponse

# Obtener y mostrar datos del catálogo con precios y filtro de rangos
def api_mostrar_catalogo(request):
    # Obtener los parámetros de rango de precios desde la solicitud GET
    precio_min = request.GET.get('precio_min', 0)  # Valor mínimo del rango de precios (por defecto 0)
    precio_max = request.GET.get('precio_max', 100000)  # Valor máximo del rango de precios (por defecto 100000)

    # Consulta para obtener los productos y filtrar por el precio de la tabla `Producto`
    productos = Producto.objects.filter(
        precio__gte=precio_min, 
        precio__lte=precio_max
    ).select_related('categoria')  # Relacionamos con la categoría si necesitamos mostrar información de la categoría

    # Renderizar los productos en el template
    return render(request, 'Productos/catalogo.html', {'productos': productos})


# Recuperar los datos de una skin seleccionada
def api_detalle_producto(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).values(
        'id', 'nombre', 'descripcion', 'stock', 'categoria__arma', 'categoria__ropa', 'juego__nombre'
    ).first()

    if producto:
        return JsonResponse(producto, safe=False)
    else:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

# Ver juegos
def api_ver_juegos(request):
    # Recupera todos los juegos desde la base de datos
    juegos = Juego.objects.all()
    # Convierte los juegos en una lista de diccionarios
    juegos_list = []
    for juego in juegos:
        juegos_list.append({
            'id': juego.id,
            'logo': juego.logo if juego.logo else None,  # Manejar el caso donde logo sea NULL
            'plataforma': juego.plataforma,
            'nombre': juego.nombre,
            'url_pagina': juego.url_pagina,
        })

    # Devuelve la lista de juegos en formato JSON
    return JsonResponse({'juegos': juegos_list})

# Implementar la lógica para filtrar y buscar skins
def api_buscar_productos(request):
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria_id', '')  # Filtro por categoría
    juego = request.GET.get('juego_id', '')  # Filtro por juego
    precio_min = request.GET.get('precio_min', 0)  # Rango de precios
    precio_max = request.GET.get('precio_max', 1000)  # Rango de precios predeterminado

    productos = Producto.objects.all().values('id', 'nombre', 'descripcion', 'categoria__arma', 'juego__nombre', 'precio')

    if query:
        productos = productos.filter(nombre__icontains=query)

    if categoria:
        productos = productos.filter(categoria_id=categoria)

    if juego:
        productos = productos.filter(juego_id=juego)

    # Filtrar por el precio de la tabla `Producto`
    productos = productos.filter(precio__gte=precio_min, precio__lte=precio_max)

    return JsonResponse(list(productos), safe=False)

# Crear el endpoint para acceder a las categorías de videojuegos desde la base de datos
def obtener_categorias(request):
    categorias = Categoria.objects.all().values('id', 'arma', 'ropa')
    return JsonResponse(list(categorias), safe=False)



