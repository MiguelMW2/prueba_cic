from flask import Flask, request, jsonify, json
from random import randint
import csv

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Mundo"

@app.route("/leer/<categoria>")
def convertirArchivo(categoria):
    data = []
    with open("noticias.json") as noticiasJSON:
        noticias = json.load(noticiasJSON)
        for noticia in noticias:
            if categoria == noticia["categoria"]:
                data.append(noticia)
    return jsonify(success=True, data=data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
