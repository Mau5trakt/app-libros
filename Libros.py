import requests
import json

class Libros():
    def __init__(self, busqueda):
        self.busqueda = busqueda
        self.link =  f"https://www.googleapis.com/books/v1/volumes?q={busqueda}"
        self.resultado = requests.get(self.link)
        self.libros = self.resultado.json()
        self.items = self.libros["items"]
        self.encoded = json.dumps(self.items)
        self.decoded = json.loads(self.encoded)
        self.rango = len(self.decoded)

        
    def titulo(self, titulo): 
        libro = self.decoded[titulo]
        return (libro["volumeInfo"]["title"])


    def descripcion(self, titulo):
        libro = self.decoded[titulo]
        try:
            return(libro["volumeInfo"]["description"])
        except:
            return("Descripcion no disponible")


    def imagen(self, titulo):
        libro = self.decoded[titulo]

        try:
            return(libro["volumeInfo"]["imageLinks"]["thumbnail"])
        except:
            return("No image")    

    def autor(self, titulo):
        libro = self.decoded[titulo]

        try:
            return(libro["volumeInfo"]["authors"][0])
        except:
            return"No author available"
        
    def url(self, titulo):
        libro = self.decoded[titulo]

        try:
            return(libro["volumeInfo"]["previewLink"])
        except:
            return("No link avaliable")


