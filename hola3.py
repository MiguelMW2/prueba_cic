import csv


palabras = {

}

with open('TodasLasNoticias.csv', 'r') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in fileReader:
        for column in row:
            lista = column.split(',')
            for palabra in lista:
                listaPalabra = palabra.split(" ")
                if listaPalabra != '':
                    palabras[listaPalabra] = 1


print(palabras)
