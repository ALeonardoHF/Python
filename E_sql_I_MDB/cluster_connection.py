import pymongo

client = pymongo.MongoClient("URI MongoCluster")
db = client.COCHES
collection = db.naves

mydict = { "nombre": "Lupillo Rivera", "direccion": "C/ Menor 43" }

x = collection.insert_one(mydict)
