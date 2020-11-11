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

file = os.path.abspath(r"C:\Users\Leonardo Heredia\Documents\Respaldo\Programacion Integrativa\Python\Exportar Importar SQL MySQL\Prueba2.json")
json_data=open(file).read()
json_obj = json.loads(json_data)

# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val
# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'root',passwd = '3312',db = 'exportar_Datos_sql')
cursor = con.cursor()

#create table to MySQL
cursor.execute("CREATE TABLE  Celulares (id_prod int PRIMARy KEY , nom_prod varchar (30) , precio int)")

# parse json data to SQL insert
for i, item in enumerate(json_obj):
    id_prod = validate_string(item.get("id_prod", None))
    nom_prod = validate_string(item.get("nom_prod", None))
    precio = validate_string(item.get("precio", None))

    cursor.execute("INSERT INTO Celulares (id_prod,	nom_prod,	precio) VALUES (%s,	%s,	%s)", (id_prod,	nom_prod,	precio))
con.commit()
con.close()
print("Terminado.......")
