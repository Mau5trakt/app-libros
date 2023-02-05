from Libros import *

respuesta = Libros("Trono De Cristal")

print(respuesta.rango)
for a in range(respuesta.rango):
    print(f"titulo {a}")
    print(respuesta.titulo(a))
    print(respuesta.descripcion(a))
    print(respuesta.imagen(a))
    print(respuesta.autor(a))
    print(respuesta.url(a))


