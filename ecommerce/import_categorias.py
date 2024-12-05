import json
from productos.models import Categoria

# Cargar los datos desde el archivo JSON
with open('categorias.json', 'r', encoding='utf-8') as f:
    categorias_data = json.load(f)

# Insertar los datos en la base de datos
for categoria_data in categorias_data:
    categoria = Categoria(
        id=categoria_data['id'],
        tipo=categoria_data['tipo']
    )
    categoria.save()

print("Categorías importadas correctamente.")
