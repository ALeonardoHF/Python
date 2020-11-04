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

xmlFile = open("Documento.xml","w")
xmlFile.write('<DATA>')

for row in rows:
    xmlFile.write('<ROW>')

    for i in range(len(cursor.description)):
        desc = cursor.description[i]
        columnName = str(desc[0])

        data = row[i]

        if data == None:
            data = ''
        xmlFile.write('<%s>%s</%s>' % (columnName, data, columnName))
    xmlFile.write('</ROW>')
xmlFile.write('</DATA>')
xmlFile.close()

print("Escritura del archivo terminada......")

#conexion con la base de datos
engine = create_engine("mysql+pymysql://root:3312@localhost/exportar_datos_sql")

conn = pymysql.connect(
  host="localhost",
  user="root",
  password="3312",
  db="exportar_datos_sql"
)

#obtener el archivo xml a importar
xtree = et.parse("Documento.xml")
xroot = xtree.getroot()

columnas = ["id_prod","nom_prod", "ver_Android","precio"]
rows = []

for node in xroot: 
    
    id_prod = node.find("id_prod").text if node is not None else None
    nombre = node.find("nom_prod").text if node is not None else None
    android = node.find("ver_Android").text if node is not None else None
    precio = node.find("precio").text if node is not None else None
    
    rows.append({"id_prod": id_prod, "nom_prod": nombre, "ver_Android": android,"precio" :precio})

Imprimir = pd.DataFrame(rows, columns = columnas)


table_name = 'celulares'
Imprimir.to_sql(table_name,con=engine)
