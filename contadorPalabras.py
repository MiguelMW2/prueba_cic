palabras = {}

archivo = open("TodasLasNoticias.csv", "r", encoding="utf8")
for noticia in archivo:
    noticia = noticia.replace(",", " ")
    lista = noticia.split(" ")
    for palabra in lista:
        palabra = palabra.replace("“", "")
        palabra = palabra.replace("”", "")
        palabra = palabra.replace("'", "")
        palabra = palabra.replace("\n", "")
        palabra = palabra.replace(" ", "")
        if palabra != "":
            if palabra not in palabras:
                palabras[palabra] = 1
            else:
                palabras[palabra] = palabras.get( str(palabra) ) + 1

print(palabras)
