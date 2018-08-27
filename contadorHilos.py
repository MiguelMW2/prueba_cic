import csv, threading

palabras = {}

def contarPalabras(listaReader):
	print(threading.currentThread().getName(), 'Lanzado')

	for archivo in listaReader:
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
	print(threading.currentThread().getName(), 'Detenido')

def hilos():


	with open("TodasLasNoticias.csv", "r", encoding="utf8") as csvfile:
		fileReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		listaReader = list(fileReader)
		lista1 = listaReader[0:61109]
		lista2 = listaReader[61109:61109*2]
		lista3 = listaReader[61109*2:61109*3]
		lista4 = listaReader[61109*3:61109*4]

	a = threading.Thread(target=contarPalabras, name='Hilo_1', args=[lista1])
	b = threading.Thread(target=contarPalabras, name='Hilo_2', args=[lista2])
	c = threading.Thread(target=contarPalabras, name='Hilo_3', args=[lista3])
	d = threading.Thread(target=contarPalabras, name='Hilo_4', args=[lista4])
	a.start()
	b.start()
	c.start()
	d.start()
	a.join()
	b.join()
	c.join()
	d.join()
	print(palabras)

hilos()
