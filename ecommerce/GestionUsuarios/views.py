import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password  # Para verificar la contraseña en la base de datos
from .models import Validacion  # Asegúrate de que esta es la clase que almacena los usuarios

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Datos JSON inválidos.'}, status=400)

        # Verificar si el correo existe en la base de datos
        try:
            usuario = Validacion.objects.get(correo=email)
            if check_password(password, usuario.contraseña):  # Verificar la contraseña
                return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso'}, status=200)
            else:
                return JsonResponse({'success': False, 'message': 'Contraseña incorrecta'}, status=401)
        except Validacion.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Correo no registrado'}, status=404)

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
