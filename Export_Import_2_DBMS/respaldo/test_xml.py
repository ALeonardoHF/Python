from sqlalchemy import create_engine
from os import environ
import pandas as pd
import pymysql
import json
import xml.etree.ElementTree as et 


#db_uri = environ.get('mysql+pymysql://root:toor@localhost:3306/futbol')
engine = create_engine("mysql+pymysql://root:3312@localhost/exportar_datos_sql")

conn = pymysql.connect(
  host="localhost",
  user="root",
  password="3312",
  db="exportar_datos_sql"
)

xtree = et.parse("Test.xml")
xroot = xtree.getroot()


df_cols = ["id_prod", "nom_prod", "ver_Android","precio"]
rows = []

for node in xroot: 
    #s_idequipo = node.attrib.get("idequipo")
    s_id = node.find("id_prod").text if node is not None else None
    s_nombre = node.find("nom_prod").text if node is not None else None
    s_android = node.find("ver_Android").text if node is not None else None
    s_precio = node.find("precio").text if node is not None else None
    
    rows.append({"id_prod": s_id, "nom_prod": s_nombre, "ver_Android": s_android,"precio" :s_precio})

out_df = pd.DataFrame(rows, columns = df_cols)

print(out_df)

table_name = 'celulares'
out_df.to_sql(table_name,con=engine)
   
   

#with open('exp.json') as json_data:    
    #d = json.load(json_data)    
    #print(d)

#df = pd.DataFrame(d)

#print(df)


#table_name = 'equipos'
#df.to_sql(table_name,con=engine)
