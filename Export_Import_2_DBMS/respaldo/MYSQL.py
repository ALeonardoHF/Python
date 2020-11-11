from sqlalchemy import create_engine
from os import environ
import pandas as pd
import pymysql
import json
import xml.etree.ElementTree as et 
import dicttoxml
import os
from xml.dom.minidom import parseString
import pyodbc
import collections


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
    d['nom_prod'] = row.nom_prod
    d['ver_Android'] = row.ver_Android
    d['precio'] = row.precio
    objects_list.append(d)
    j = json.dumps(objects_list) 
    with open("Prueba2.json","w") as f:
        f.write(j)

conn.close()

print("Terminado.......")




file = os.path.abspath(r"C:\Users\Leonardo Heredia\Documents\Respaldo\Programacion Integrativa\Python\Exportar Importar SQL MySQL\Prueba2.json")
json_data=open(file).read()
obj = json.loads(json_data)
#print(obj)
{u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
xml = dicttoxml.dicttoxml(obj)
print(xml)
dom = parseString(xml)
print(dom.toprettyxml())
with open ("Documento.xml","w+") as f:
    f.write(dom.toprettyxml()) 


#db_uri = environ.get('mysql+pymysql://root:toor@localhost:3306/futbol')
engine = create_engine("mysql+pymysql://root:3312@localhost/exportar_datos_sql")

conn = pymysql.connect(
  host="localhost",
  user="root",
  password="3312",
  db="exportar_datos_sql"
)

xtree = et.parse("Documento.xml")
xroot = xtree.getroot()


columnas = ["nom_prod", "ver_Android","precio"]
rows = []

for node in xroot: 
    
    
    nombre = node.find("nom_prod").text if node is not None else None
    android = node.find("ver_Android").text if node is not None else None
    precio = node.find("precio").text if node is not None else None
    
    rows.append({"nom_prod": nombre, "ver_Android": android,"precio" :precio})

Imprimir = pd.DataFrame(rows, columns = columnas)

#print(out_df)

table_name = 'celulares'
Imprimir.to_sql(table_name,con=engine)
