from sqlalchemy import create_engine
import pandas as pd
import pymysql
import xml.etree.ElementTree as et 
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

xmlFile = open("MEJORESTE.xml","w")
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

#conexion a mysql
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
 

print(Imprimir)

table_name = 'tabla_referencia'
Imprimir.to_sql(table_name,con=engine)

# connect to MySQL - esto lo hago para acomodar las columnas como yo quiero, desde una tabla con columnas de mas
con = pymysql.connect(host = 'localhost',user = 'root',passwd = '3312',db = 'exportar_Datos_sql')
cursor = con.cursor()

#querys de mysql - instrucciones
cursor.execute("CREATE TABLE celulares SELECT nom_prod,ver_Android,precio FROM tabla_referencia;")
cursor.execute("DROP TABLE tabla_referencia;")

print("Terminado.......")
