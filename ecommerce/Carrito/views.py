from django.shortcuts import render
from django.shortcuts import redirect



def carrito(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        #Ojo aca. Usamos el metodo redirect, que lo que hace es enviarnos a la URL con el name='metodo_pago_x'
        #cuando se necesita cambiar de url porque nos dirigimos a otra pagina se usa redirect y no render.
        #al movernos a esa nueva URL, se llama a la funcion def metodo_pago_x.
        if metodo_pago == '1':
            return redirect('pagos:metodo_pago_1')
        elif metodo_pago == '2':
            return redirect('pagos:metodo_pago_2')
    return render(request,"Carrito/carrito.html")  # Aquí iría la lógica para mostrar el contenido del carrito




def agregar_al_carrito(request, producto_id):
    pass  # Aquí iría la lógica para agregar un producto al carrito


