Análisis de la Función registerUser
Formato de Respuesta:

La función está diseñada para devolver resultados en formato JSON, lo que es estándar para las APIs.
Importaciones:

Se importan las bibliotecas necesarias: json para manejar datos en formato JSON, JsonResponse para enviar respuestas en formato JSON y el modelo Validacion para interactuar con la base de datos.
Verificación del Método de Solicitud:

Se comprueba que la solicitud sea de tipo POST. Si no es así, se devuelve un mensaje de error con el código 405 (Método no permitido).
Manejo de Errores en JSON:

Se utiliza un bloque try-except para manejar posibles errores al decodificar el JSON. Si ocurre un JSONDecodeError, se responde con un mensaje de error y un código de estado 400.
Obtención de Datos:

Se obtienen los datos del cuerpo de la solicitud usando data.get(), lo que permite manejar la ausencia de claves sin causar un error.
Comprobación de Existencia de Correo:

Se utiliza Validacion.objects.filter(correo=mail).exists() para verificar si el correo ya está registrado en la base de datos. Si existe, se responde con un mensaje de error y un código 409.
Creación de Nuevo Usuario:

Si el correo no existe, se crea un nuevo objeto Validacion, se usa make_password para asegurar la contraseña, y se guarda en la base de datos.
Respuesta de Éxito:

Después de registrar al nuevo usuario, se responde con un mensaje de éxito y un código de estado 201.

//agregamos const REGISTER_URL = '/registro/'; ya que nos daba error ya que no sabia a que url ir a buscar los datos