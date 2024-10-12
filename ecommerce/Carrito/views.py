from django.shortcuts import render
from django.shortcuts import redirect

#Integracion carrito
import mercadopago
from django.conf import settings
from django.shortcuts import render

def carrito(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_pago')
        #Ojo aca. Usamos el metodo redirect, que lo que hace es enviarnos a la URL con el name='metodo_pago_x'
        #cuando se necesita cambiar de url porque nos dirigimos a otra pagina se usa redirect y no render.
        #al movernos a esa nueva URL, se llama a la funcion def metodo_pago_x.
        if metodo_pago == '1':
            return redirect('metodo_pago_1')
        elif metodo_pago == '2':
            return redirect('metodo_pago_2')
    return render(request,"Carrito/carrito.html")  # Aquí iría la lógica para mostrar el contenido del carrito

def metodo_pago_1(request):
    return render(request,"Carrito/metodoPago1.html")

def metodo_pago_2(request):
    return render(request,"Carrito/metodoPago2.html")


def agregar_al_carrito(request, producto_id):
    pass  # Aquí iría la lógica para agregar un producto al carrito



def metodo_pago_mercadopago(request):
    # Inicializar el SDK de MercadoPago con el access_token
    sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

    # Crear la preferencia de pago
    preference_data = {
        "items": [
            {
                "title": "Producto Ejemplo",
                "quantity": 1,
                "unit_price": 100.00
            }
        ],
        "back_urls": {
            "success": "http://tu-dominio.com/success",
            "failure": "http://tu-dominio.com/failure",
            "pending": "http://tu-dominio.com/pending"
        },
        "auto_return": "approved",  # Redirecciona automáticamente al éxito si el pago es aprobado
    }

    preference_response = sdk.preference().create(preference_data)  # Creación de la preferencia
    preference = preference_response["response"]

    # Pasamos la public_key al template junto con la preferencia ID
    context = {
        "preference_id": preference['id'],
        "public_key": settings.MERCADO_PAGO_PUBLIC_KEY
    }

    return render(request, 'Carrito/checkout.html', context)
