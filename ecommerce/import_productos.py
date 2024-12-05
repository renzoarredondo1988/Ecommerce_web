import json
from productos.models import Producto  # Reemplaza con la ruta de tu modelo

# Carga el archivo JSON
with open('productos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Itera sobre los datos y crea objetos
for item in data:
    producto = Producto(
        id=item['id'],  # Si necesitas mantener el mismo ID
        stock=item['stock'],
        nombre=item['nombre'],
        categoria_id=item['categoria_id'],  # Usa _id si es clave foránea
        juego_id=item['juego_id'],  # Usa _id si es clave foránea
        precio=item['precio'],
        descripcion=item['descripcion'],
        imagen=item['imagen']
    )
    producto.save()  # Guarda en la base de datos

print("Datos importados correctamente.")
