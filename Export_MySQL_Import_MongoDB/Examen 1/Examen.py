import pyodbc
import json
import collections
import pymysql, os
from pymongo import MongoClient

connstr = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Alcohol;'
print("Conectado a la base de dastos \n\n\n")
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
print("Realizando la Consulta:  \n\n\n")
cursor.execute("""
            SELECT user_id,screen_name,location,followers_count,friends_count
            FROM users
            """)
rows = cursor.fetchall()
# Convert query to row arrays
rowarray_list = []
for row in rows:
    t = (row.user_id, row.screen_name, row.location, row.followers_count, row.friends_count)
    rowarray_list.append(t)
    j = json.dumps(rowarray_list)
    
#print (f, j)
# Convert query to objects of key-value pairs
objects_list = []
print("Generando archivo Examen.json \n\n\n")
for row in rows:
    d = collections.OrderedDict()
    d['user_id'] = row.user_id
    d['screen_name'] = row.screen_name
    d['location'] = row.location
    d['followers_count'] = row.followers_count
    d['friends_count'] = row.friends_count
    objects_list.append(d)
    j = json.dumps(objects_list) 
    with open("Examen.json","w") as f:
        f.write(j)
print("Archivo generado con exito.!!! \n\n\n")
conn.close()
print("Cerrando Conexion.!! \n\n\n")

print("Conectando con MongoDB.!!! \n\n\n")
client = MongoClient('localhost', 27017)
db = client['Examen']
collection_currency = db['users']

print("Extrayendo informacion de Examen.json .!!!! \n\n\n")

with open('Examen.json') as f:
    file_data = json.load(f)

# if pymongo < 3.0, use insert()
#collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
#collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
collection_currency.insert_many(file_data)
print("Insertado con exito el documento.!!!! \n\n\n")
client.close()
print("Cerrando conexion con MongoDB.!! \n\n\n")
print("Hasta luego..!!!")


