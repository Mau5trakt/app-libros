from flask import Flask, render_template, request
from Libros import *

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        try:
            libro = request.form.get("libro")
            respuesta = Libros(libro)
            rango = respuesta.rango
            return render_template("respuesta.html", respuesta=respuesta, rango=rango)
        except:
            return render_template("index.html")

    return render_template("index.html")