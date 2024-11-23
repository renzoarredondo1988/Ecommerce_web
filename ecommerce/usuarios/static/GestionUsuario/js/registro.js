/*const REGISTER_URL = '/usuarios/';
const formRegister = document.getElementById("formRegister");

formRegister.addEventListener('submit', (event) => {
    event.preventDefault();
    registerUser();
    formRegister.reset();
});

const registerUser = () => {
    // Obtener valores y validaciones como antes...
    
    const data = {
        nombre: document.getElementById('register_name').value,
        apellido: document.getElementById('register_lastname').value,
        pais: document.getElementById('register_country').value,
        correo: document.getElementById('register_email').value,
        contraseña: document.getElementById('register_password').value,
    };

    // Obtener el token CSRF del documento
    const csrftoken = getCookie('csrftoken');

    fetch(REGISTER_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Incluir el token CSRF
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result.success);
        if (result.success === true) {
            viewAlert("Se ha registrado un usuario nuevo", "Bienvenido!");
        } else {
            viewAlert("No se ha registrado un usuario nuevo", "Algo ha salido mal. Intenta de nuevo");
            console.error(result.error);
        }
    })
    .catch(error => {
        console.error(error);
        viewAlert("Error!", "Algo ha salido mal. Intenta de nuevo");
    });
}

// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const REGISTER_URL = '/usuarios/';
const formRegister = document.getElementById("formRegister")
formRegister.addEventListener('submit', (event) => {
    event.preventDefault();
    registerUser();
    formRegister.reset()
});

const registerUser = () => {
    let nombre = document.getElementById('register_name').value;
    const validNombre = /^[A-Za-z\s]+$/;
    if (!validNombre.test(nombre)) { //validación del nombre
        viewAlert("Error", "El nombre solo debe contener letras.");
        return; // Detiene el envío del formulario
    }

    let apellido = document.getElementById('register_lastname').value;
    const validApellido = /^[A-Za-z\s]+$/;
    if (!validApellido.test(apellido)) { //validación del apellido
        viewAlert("Error", "El apellido solo debe contener letras.");
        return; // Detiene el envío del formulario
    }

    let pais = document.getElementById('register_country').value;

    let correo = document.getElementById('register_email').value;
    const validCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!validCorreo.test(correo)) {
        viewAlert("Error", "Por favor, ingresa un correo válido.");
        return;
    }

    let contraseña = document.getElementById('register_password').value;
    const validContraseña = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/; // Al menos 8 caracteres, una letra y un número
    if (!validContraseña.test(contraseña)) {
        viewAlert("Error", "La contraseña debe tener al menos 8 caracteres, incluyendo una letra y un número.");
        return;
    }

    let confirmar_contraseña = document.getElementById('confirm_password').value;
    if (contraseña !== confirmar_contraseña) {
        viewAlert("Error", "Las contraseñas no coinciden. Intenta de nuevo");
        return;
    }

    console.log(nombre, apellido, pais, correo, contraseña, confirmar_contraseña);

    const data = {
        nombre: nombre,
        apellido: apellido,
        pais: pais,
        correo: correo, 
        contraseña: contraseña,
    };

    fetch(REGISTER_URL, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result.success);
        if(result.success === true){
            viewAlert("Se ha registrado un usuario nuevo", "Bienvenido!");
        } else{
            viewAlert("No se ha registrado un usuario nuevo", "Algo ha salido mal. Intenta de nuevo");
            console.error(result.error);
        }
    })
    .catch(error => {
        console.error(error);
        viewAlert("Error!", "Algo ha salido mal. Intenta de nuevo");
    })
}*/