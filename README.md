<h2 align="center" >🐝 CodeHive ecommerce 🐝</h2>

<p align="center">CodeHive es una plataforma de comercio electrónico desarrollada con Django que permite a los usuarios navegar, buscar y comprar productos. La aplicación incluye funcionalidades como carrito de compras y autenticación de usuario. Esta plataforma está diseñada para ser fácil de usar y expandir, ideal para negocios pequeños y medianos que desean tener presencia en línea. ¡Espero que disfrutes tanto de ella utilizandola como nosotros desarrollandola!</p>
<br>
<details>
  <summary><h3>Características</h3></summary>  
    <ul>
      <li>Autenticación de usuarios: Registro, inicio de sesión, cierre de sesión y recuperación de contraseña para usuarios registrados.</li>
      <li>Gestión de productos: Posibilidad de agregar, editar y eliminar productos (solo accesible para administradores desde el panel admin de Django).</li>
      <li>Carrito de compras: Los usuarios pueden añadir productos al carrito, ver el resumen de su carrito y modificar la cantidad de cada artículo.</li>
      <li>Interfaz de usuario intuitiva: Diseño de navegación claro y fácil de usar, adaptable a dispositivos móviles.</li>
      <li>Sistema de notificaciones: Notificación de éxito al realizar una compra o completar alguna acción relevante en la plataforma.</li>
      <li>Catálogo de productos: Visualización de productos organizada en categorías, con opciones de filtrado y paginación para facilitar la navegación por todo el inventario disponible.</li>
    </ul>  
    
</details>

<details>
  <summary><h3>Tecnologías Usadas</h3></summary>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/>  
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
<img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/>
</details>

<details>  
<summary><h3>Instalación</h3></summary>
<ol>
  <li>
    <h4>Clona este repositorio:</h4>
    
    git clone https://github.com/CodeStrong2023/CodeHive-EC.git
        
  </li>
  <li>
    <h4>Navega al directorio del proyecto:</h4>
    
    cd CodeHive-EC
        
  </li>
  <li>
    <h4>Entrar al entorno virtual desde PowerShell:</h4>
  
    source .\.venv\Scripts\activate.ps1 

  </li>  
  <li>
    <h4>Ingresar a la carpeta "ecommerce":</h4>
    
    cd ecommerce
        
  </li>
  <li>
    <h4>Aplica las migraciones para configurar la base de datos:</h4>
    
    python manage.py migrate

  </li>
  <li>
    <h4>Cargar archivos estáticos (opcional):</h4>
    
    python manage.py collectstatic

  </li>
  <li>
    <h4>Inicia el servidor de desarrollo:</h4>
    
    python manage.py runserver

  </li>
</ol>
</details>

<details>  
  <summary><h3>Guía de uso</h3></summary>

  - **Acceso al proyecto:** Una vez que el servidor esté corriendo _(python manage.py runserver)_, abre tu navegador y navega a _http://127.0.0.1:8000/_ para acceder a la aplicación.
    
  - **Registrar una cuenta:** Para poder acceder a funcionalidades como el carrito de compras, es necesario registrarse. Haz clic en "Sign In" para crear una cuenta de usuario.

  - **Explorar el catálogo:** Navega por el catálogo de productos en la sección "Productos". Aquí puedes ver todos los productos disponibles, con la opción de filtrarlos por categoría y por precio.

  - **Agregar productos al carrito:** Cuando encuentres productos de interés, puedes añadirlos a tu carrito de compras para continuar con la compra. Accede al carrito en cualquier momento desde el menú principal.

  - **Realizar un pedido:** Después de agregar productos al carrito, ve a la página del carrito y sigue el proceso para realizar un pedido.

  - **Cerrar sesión:** Si has iniciado sesión, puedes cerrar sesión desde el menú en la parte superior derecha de la página haciendo clic en "Log Out".
</details>

<details>
  <summary><h3>Contribución</h3></summary>
<ol>
  <li>
    <h4>Fork este repositorio</h4>
    <p>Haz un "fork" del repositorio para tener una copia personal del proyecto.</p>
  </li>
  <li>
    <h4>Clona tu fork</h4>    
    <p>Clona tu repositorio forked a tu máquina local:</p>
    
    git clone https://github.com/CodeStrong2023/CodeHive-EC.git
        
  </li>
  <li>
    <h4>Crea una nueva rama</h4>    
    <p>Antes de hacer cambios, crea una nueva rama:</p>
    
    git checkout -b nombre-de-tu-rama
        
  </li>
  <li>
    <h4>Realiza tus cambios</h4>
    <p>Haz las modificaciones que desees en el código.</p>
  </li>
  <li>
    <h4>Haz commit de tus cambios</h4>    
    <p>Una vez hayas terminado, haz commit de tus cambios con un mensaje descriptivo:</p>
    
    git commit -m "Descripción de los cambios realizados"
        
  </li>
  <li>
    <h4>Sube tus cambios a tu fork</h4>    
    <p>Sube tus cambios a tu fork en GitHub:</p>
    
    git push origin nombre-de-tu-rama
        
  </li>
  <li>
    <h4>Envía un pull request</h4>
    <p>Ve a la página de tu repositorio en GitHub y haz un pull request para que tus cambios sean revisados y fusionados con el repositorio principal.</p>
  </li>
  <li>
    <h4>Reportar issues</h4>
    <p>Si encuentras algún error o problema, abre un "issue" en GitHub detallando el problema encontrado.</p>
  </li>
</details>

<details>    
  <summary><h3>Dream Team</h3></summary>
  <p>Este proyecto fue desarrollado como parte del proyecto final para la Tecnicatura Universitaria en Programación dada por la <a href="https://www.frsr.utn.edu.ar/">UTN FRSR</a>.</p>

  - <a href="https://github.com/AndresPampa">Andrés Ábdala</a>&nbsp;&nbsp;&nbsp;&nbsp;

  - <a href="https://github.com/renzoarredondo1988">Renzo Arredondo</a>&nbsp;&nbsp;&nbsp;&nbsp;

  - <a href="https://github.com/Flor-balladares">Florencia Balladares</a>&nbsp;&nbsp;&nbsp;&nbsp;

  - <a href="https://github.com/GiulianaDeEt">Giuliana Dealbera</a>&nbsp;&nbsp;&nbsp;&nbsp;

  - <a href="https://github.com/Tiago0613">Tiago Ibarrola</a>&nbsp;&nbsp;&nbsp;&nbsp;

  - <a href="https://github.com/YESS-BAIT-LEJEM">Yassica Reynoso</a>&nbsp;&nbsp;&nbsp;&nbsp;

  <p>¡Agradecemos a todos los involucrados por su esfuerzo y dedicación en el desarrollo de este proyecto!🫶</p>
</details>
