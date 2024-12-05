import json
from productos.models import Juego

# Cargar los datos desde el archivo JSON
with open('juego.json', 'r', encoding='utf-8') as f:
    juegos_data = json.load(f)

# Insertar los datos en la base de datos
for juego_data in juegos_data:
    juego = Juego(
        id=juego_data['id'],
        nombre=juego_data['nombre'],
        plataforma=juego_data['plataforma'],
        url_pagina=juego_data['url_pagina'],
        logo=juego_data.get('logo', None)  # Usamos None si no hay valor de 'logo'
    )
    juego.save()

print("Juegos importados correctamente.")
