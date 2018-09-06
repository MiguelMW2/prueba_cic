import json, csv

def ini():
    data = []
    with open("TodasLasNoticias.csv", "r", encoding="utf8") as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for noticia in fileReader:
            listaNoticias = {}
            # if len(noticia) == 5:
            #     listaNoticias["fecha"] = noticia[0]
            #     listaNoticias["titulo"] = noticia[1]
            #     listaNoticias["url"] = noticia[2]
            #     listaNoticias["descripcion"] = noticia[3]
            #     listaNoticias["categoria"] = noticia[4]
            # el
            if len(noticia) >= 5:
                listaNoticias["fecha"] = noticia[0]
                listaNoticias["titulo"] = noticia[1]
                listaNoticias["url"] = noticia[2]
                listaNoticias["descripcion"] = noticia[3]
                for i in range(4, len(noticia)):
                    listaNoticias["descripcion"] = listaNoticias["descripcion"] + noticia[i-1]
                listaNoticias["categoria"] = noticia[len(noticia) - 1]
            if bool(listaNoticias):
                data.append(listaNoticias)
    with open('noticias.json', 'w') as outfile:
        json.dump(data, outfile)

ini()