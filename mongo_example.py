import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017,username='root',password='Cic1234*',authSource="admin")
db = client["test"]
collection = db["data"]

keys = {}
cont = 0
docs = collection.find()
for document in docs:
	cont = cont + 1
	for key in document.keys():
		if key not in keys:
			keys[key] = 1
		else:
			keys[key] = keys[key] + 1

for key in keys:
	keys[key] = keys[key] / cont * 100
	print(key, str(keys[key]) + "%")
