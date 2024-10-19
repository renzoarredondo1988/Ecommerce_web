import json  # Importamos el módulo json para trabajar con datos en formato JSON
from django.http import JsonResponse  # Importamos JsonResponse para enviar respuestas JSON
from django.shortcuts import render
from .models import Validacion  # Importamos el modelo Validacion
from django.contrib.auth.hashers import make_password  # Importamos para hash de contraseñas
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def registerUser(request):
    
    if request.method == 'POST':  # Verificamos que el método de la solicitud sea POST
        try:
            data = json.loads(request.body)  # Cargamos los datos del cuerpo de la solicitud en formato JSON
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Datos JSON inválidos.'}, status=400)

        mail = data.get('correo')  # Obtenemos el correo del JSON
        contraseña = data.get('contraseña')  # Obtenemos la contraseña del JSON

        if Validacion.objects.filter(correo=mail).exists():  # Comprobamos si el correo ya existe en la base de datos
            return JsonResponse({'success': False, 'message': 'El correo ya está registrado.'}, status=409)

        # Creamos un objeto de tipo Validacion con los datos obtenidos
        nuevoUsuario = Validacion(correo=mail, contraseña=make_password(contraseña))  # Guardamos la contraseña de manera segura
        nuevoUsuario.save()  # Guardamos el nuevo usuario en la base de datos

        # Enviamos la respuesta de éxito al front con el código 201
        return JsonResponse({'success': True, 'message': 'Usuario registrado correctamente'}, status=201)

    # Si no es un método POST, devolvemos un error 405 (Method Not Allowed)
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
    return render(request,'GestionUsuarios/registro.html')




        

