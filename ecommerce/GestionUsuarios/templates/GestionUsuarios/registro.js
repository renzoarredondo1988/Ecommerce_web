const formRegister = document.getElementById("formRegister")
formRegister.addEventListener('submit', (event) => {
    event.preventDefault();
    registerUser();
    formRegister.reset()
});

const registerUser = () => {
    let nombre = document.getElementById('register_name').value;
    let apellido = document.getElementById('register_lastname').value;
    let pais = document.getElementById('register_country').value;
    let correo = document.getElementById('register_email').value;
    let contraseña = document.getElementById('register_password').value;
    let confirmar_contraseña = document.getElementById('confirm_password').value;

    console.log(nombre, apellido, pais, correo, contraseña, confirmar_contraseña);

    const data = {
        nombre: nombre,
        apellido: apellido,
        pais: pais,
        correo: correo,
        contraseña: contraseña,
    };

    fetch(REGISTER_URL, {
        method: 'POST',
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
}


