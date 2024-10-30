from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import redirect

#Integracion carrito
import mercadopago
from django.conf import settings
from django.shortcuts import render




def metodo_pago_1(request):
    return render(request,"pagos/metodoPago1.html")

def metodo_pago_2(request):
    return render(request,"pagos/metodoPago2.html")



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

    return render(request, 'pagos/checkout.html', context)
