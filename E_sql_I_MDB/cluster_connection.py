import pymongo

client = pymongo.MongoClient("mongodb+srv://Admin:3312@proyectofinal.yytqy.mongodb.net/ProFinal?retryWrites=true&w=majority")
db = client.COCHES
collection = db.naves

mydict = { "nombre": "Lupillo Rivera", "direccion": "C/ Menor 43" }

x = collection.insert_one(mydict)
