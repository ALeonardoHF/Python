import pyodbc
import json
import collections
import pymysql, os

connstr = 'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=Alcohol;'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
cursor.execute("""
            SELECT id_prod,nom_prod,ver_Android,precio
            FROM Celulares
            """)
rows = cursor.fetchall()
# Convert query to row arrays
rowarray_list = []
for row in rows:
    t = (row.id_prod, row.nom_prod, row.ver_Android, row.precio)
    rowarray_list.append(t)
    j = json.dumps(rowarray_list)
with open('Prueba.json','w') as f:
    f.write(j)
#print (f, j)
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['id_prod'] = row.id_prod
    d['nom_prod'] = row.nom_prod
    d['ver_Android'] = row.ver_Android
    d['precio'] = row.precio
    objects_list.append(d)
    j = json.dumps(objects_list) 
    with open("Prueba2.json","w") as f:
        f.write(j)

conn.close()

print("Terminado.......")
