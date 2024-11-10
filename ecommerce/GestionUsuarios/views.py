import json  # Importamos el módulo json para trabajar con datos en formato JSON
from django.http import JsonResponse  # Importamos JsonResponse para enviar respuestas JSON
from django.shortcuts import redirect, render
from .models import Validacion, Usuario  # Importamos el modelo Validacion
from django.contrib.auth.hashers import make_password,check_password   # Importamos para hash de contraseñas
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        mail = request.POST.get('register_email')
        contraseña = request.POST.get('register_password')
        confirmarContraseña = request.POST.get('confirm_password')
        
        # Verificar si las contraseñas coinciden
        if contraseña != confirmarContraseña:
            return render(request, 'GestionUsuarios/registro.html', {
                'error': 'Las contraseñas no coinciden. Vuelva a intentarlo',
                'register_password': contraseña
            })

        # Verificar si el correo ya existe
        if Validacion.objects.filter(correo=mail).exists():
            return JsonResponse({'success': False, 'message': 'El correo ya está registrado.'}, status=409)

        # Crear el objeto Validacion y guardarlo
        nuevo_usuario_validacion = Validacion(
            correo=mail,
            contraseña=make_password(contraseña)
        )
        nuevo_usuario_validacion.save()

        # Crear el objeto Usuario y asociarlo con el objeto de Validacion
        nombre = request.POST.get('register_name')  # Nombre ingresado en el formulario de registro
        apellido = request.POST.get('register_lastname')
        pais = request.POST.get('register_country')
        
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            pais=pais,
            validacion=nuevo_usuario_validacion  # Asociar el objeto de Validacion
        )
        nuevo_usuario.save()

        # enviamos por contxto los datos recuperados del formulario
        return render(request, 'GestionUsuarios/confirmacion.html', {
            'mensaje': 'Usuario registrado correctamente',
            'nombre': nombre,
            'apellido': apellido
        })

    return render(request, 'GestionUsuarios/registro.html')





@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')

        try:
            # Buscar al usuario en Validacion
            usuario_validacion = Validacion.objects.get(correo=email)
            if check_password(password, usuario_validacion.contraseña):
                # Obtener el usuario completo en Usuario usando la relación
                usuario = Usuario.objects.get(validacion=usuario_validacion)#busco en la tabla usuario en el atributo validacion
                #loq ue coincida con mi usuario validacion, es decir el mail y contraseña

                # Guardar datos en la sesión
                #con req.sessionobtenemos los datos de las cookies y lso cmabiamos po los atributos de usuario
                request.session['user_id'] = usuario.id
                request.session['user_email'] = usuario_validacion.correo
                request.session['username'] = usuario.nombre
                request.session['user_apellido'] = usuario.apellido
                request.session['user_pais'] = usuario.pais

                #request.session.modified = True

                #print(request.session)

                return render(request, 'InterfazGeneral/index.html', {
                'mensaje': 'Inicio de sesion correcto',
                
            })
            else:
                return render(request, 'GestionUsuarios/login.html', {
                    'error_message': 'Contraseña incorrecta.'
                })
        except Validacion.DoesNotExist:
            return render(request, 'GestionUsuarios/login.html', {
                'error_message': 'Correo no registrado.'
            })

    return render(request, 'GestionUsuarios/login.html')


def testeo(request):
    return render(request, 'GestionUsuarios/testeo.html')

def logout_user(request):
    request.session.flush()  # Esto elimina todos los datos de la sesión

    # Obtener la URL de la que vino el usuario (o la home si no se encuentra)
    return redirect(request.META.get('HTTP_REFERER', 'interfaz_general:home'))
