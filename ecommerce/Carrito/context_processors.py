# carro/context_processors.py

def auth_and_cart_info(request):
    # Inicializar variables
    authenticated = False
    user_id = None
    user_email = None
    user_name = None
    total = 0

    # Verificar si el usuario está autenticado
    if request.session.get('user_id'):  # Verificamos si hay un user_id en la sesión
        authenticated = True
        user_id = request.session['user_id']  # Guardamos el ID del usuario en la variable
        user_email = request.session['user_email']  # Guardamos el correo del usuario
        user_name = request.session['username']  # Guardamos el nombre del usuario

        # Calcular el total del carrito
        if 'carro' in request.session:
            for item in request.session['carro'].values():
                total += float(item['precio']) * item.get('cantidad', 1)  # Multiplicamos por cantidad si existe

    return {
        'authenticated': authenticated, #{% if request.session.authenticated %}
        'user_id': user_id,
        'user_email': user_email,
        'user_name': user_name,
        'importe_total_carro': total,
    }