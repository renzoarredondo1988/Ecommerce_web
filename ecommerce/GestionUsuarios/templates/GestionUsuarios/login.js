const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const LOGIN_URL = "{% url 'inicio_sesion' %}";

const formLogin = document.getElementById("formLogin")
formLogin.addEventListener('submit', (event) => {
    event.preventDefault();
    loginUser();
    formLogin.reset()
});

const loginUser = () => {
    let correo = document.getElementById('login_email').value;
    let contraseña = document.getElementById('login_password').value;

    console.log(correo, contraseña);

    const data = {
        correo: correo,
        contraseña: contraseña,
    };

    fetch(LOGIN_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result.success);
        if(result.success === true){
            viewAlert("Haz iniciado sesión", "Bienvenido!");
        } else{
            viewAlert("Ups...", "Algo ha salido mal. Intenta de nuevo");
            console.error(result.error);
        }
    })
    .catch(error => {
        console.error(error);
        viewAlert("Error!", "Algo ha salido mal. Intenta de nuevo");
    })
}


