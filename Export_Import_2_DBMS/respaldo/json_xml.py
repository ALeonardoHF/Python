import json
import urllib
import dicttoxml
import os
from xml.dom.minidom import parseString
file = os.path.abspath(r"C:\Users\Leonardo Heredia\Documents\Respaldo\Programacion Integrativa\Python\Exportar Importar SQL MySQL\Prueba2.json")
json_data=open(file).read()
obj = json.loads(json_data)
print(obj)
{u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
xml = dicttoxml.dicttoxml(obj)
print(xml)
dom = parseString(xml)
print(dom.toprettyxml())
with open ("Documento.xml","w+") as f:
    f.write(dom.toprettyxml()) 




