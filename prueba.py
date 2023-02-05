import requests
import json

nombre = "Harry_Potter"

busqueda = f"https://www.googleapis.com/books/v1/volumes?q={nombre}"

resultado = requests.get(busqueda)

libros = resultado.json()
#print(len(libros))
items = libros["items"]

encoded = json.dumps(items)
decoded = json.loads(encoded)

print(len(decoded))

for a in range(len(decoded)):
    print(decoded[a]["volumeInfo"]["previewLink"])