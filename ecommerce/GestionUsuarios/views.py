import json  # Importamos el módulo json para trabajar con datos en formato JSON
from django.http import JsonResponse  # Importamos JsonResponse para enviar respuestas JSON
from django.shortcuts import redirect, render
from .models import Validacion  # Importamos el modelo Validacion
from django.contrib.auth.hashers import make_password,check_password   # Importamos para hash de contraseñas
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def registerUser(request):
   
    if request.method == 'POST':  # Verificamos que el método de la solicitud sea POST
        print(request.body.decode('utf-8')) #sin la aclaracion em mostraria solo bits
        #try:
            #data = json.loads(request.body)
        #print(data)  # Cargamos los datos del cuerpo de la solicitud en formato JSON
        #except json.JSONDecodeError:
            #return JsonResponse({'success': False, 'message': 'Datos JSON inválidos.'}, status=400)
        
        mail =  request.POST.get('register_email')   # obtenemso el crudo del html xD
        contraseña = request.POST.get('register_password') 
        confirmarContraseña=request.POST.get('confirm_password')

        if contraseña != confirmarContraseña:
            #return JsonResponse({'success': False, 'message': 'Contraseña incorrecta.'}, status=409)
          return render(request, 'GestionUsuarios/registro.html', {
                'error': 'Las contraseñas no coinciden.Vuelva a intentarlo',
                'register_password': contraseña  # Volver a rellenar el campo de correo
            })

        if Validacion.objects.filter(correo=mail).exists():  # Comprobamos si el correo ya existe en la base de datos
            return JsonResponse({'success': False, 'message': 'El correo ya está registrado.'}, status=409)

        # Creamos un objeto de tipo Validacion con los datos obtenidos
        nuevoUsuario = Validacion(correo=mail, contraseña=make_password(contraseña))  # Guardamos la contraseña de manera segura
        nuevoUsuario.save()  # Guardamos el nuevo usuario en la base de datos

        # Enviamos la respuesta de éxito al front con el código 201
        return JsonResponse({'success': True, 'message': 'Usuario registrado correctamente'}, status=201)

    # Si no es un método POST, devolvemos un error 405 (Method Not Allowed)
   
    return render(request,'GestionUsuarios/registro.html')




@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')

        try:
            usuario = Validacion.objects.get(correo=email) #instancia de validacion
            if check_password(password, usuario.contraseña):  # Verificar la contraseña
                usuario_objeto = usuario.usuario #
                request.session['user_id'] = usuario_objeto.id  # Guardamos el ID del usuario en la sesión
                request.session['user_email'] = usuario.correo  # Guardamos el correo de Validacion
                request.session['username'] = usuario_objeto.nombre  # Guardamos el nombre del usuario
                return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso'}, status=200)
            else:
                return render(request, 'GestionUsuarios/login.html', {
                    'error_message': 'Contraseña incorrecta.'
                })
        except Validacion.DoesNotExist:
            return render(request, 'GestionUsuarios/login.html', {
                'error_message': 'Correo no registrado.'
            })
        
        
#guardamso aca los nuevos usuario?
#comentar en la meet
#cerrar
    return render(request, 'GestionUsuarios/login.html')



def logout_user(request):
    if request.method == 'POST':
        request.session.flush()  # Elimina todos los datos de la sesión
        return JsonResponse({'success': True, 'message': 'Sesión cerrada correctamente'}, status=200)

    return redirect('')  # Redirige a la página de inicio
