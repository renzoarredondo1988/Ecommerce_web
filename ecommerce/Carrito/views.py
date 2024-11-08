from django.shortcuts import render
from django.shortcuts import redirect
from .carrito import Carro
from GestionUsuarios.models import Producto
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


def carrito(request):

     productos=Producto.objects.all()
     return render(request, "Carrito/carrito.html", {"productos": productos})#en el render de tienda.html, podre 
#acceder a los atributos del objeto productos, que se envian dentro de un dicc con la clave "productos"

def agregar_producto(request,producto_id): #producto_id proviene de la URL que se llama al acceder a esta vista.

    carro=Carro(request) #Cada vez que necesitas interactuar con el carrito, creas una nueva instancia
    #de Carro. Esto es necesario porque cada vez que un usuario realiza una acción (como agregar un
    #  producto), quieres acceder y modificar el carrito en función de la sesión actual del usuario.
    #Es decir, en cada interaccion se llama al constructor y se "sobreescriben" los datos del objeto carro

    producto=Producto.objects.get(id=producto_id) #Esta línea busca un objeto Producto en la base de datos
    #cuyo id coincide con el producto_id que se pasó como argumento.

    producto.precio = float(producto.precio)

    carro.agregar(producto=producto)#Usas producto=producto para indicar que el argumento producto de la
    #función agregar debe recibir el objeto producto que acabas de recuperar de la base de datos.

    # Redirige a la misma página en la que se encuentra el usuario, pasando el producto_id como parte de la URL
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def eliminar_producto(request,producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def restar_producto(request,producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def limpiar_carro(request,producto_id):
    
    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("carrito")






"""
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


"""




