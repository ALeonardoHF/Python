from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client['Examen']
collection_currency = db['usuarios']
 
def menu():
    os.system('cls') 
    print ("Selecciona una opción")
    print ("\t1 - Imprimir Base de Datos")
    print ("\t2 - Insertar Documento")
    print ("\t3 - Actualizacion de Documento")
    print ("\t4 - Eliminacion Documento")
    print ("\t5 - salir")
    
 
while True:
    # Mostramos el menu
    menu()
     
    # solicituamos una opción al usuario
    opcionMenu = input("Ingresa una opcion >> ")
 
    if opcionMenu=="1":
        print ("Imprimir Base de Datos: \n")
        print("Modo de Busqueda ?: ")
        print("\t 1.Todo    2.Especifico\n")
        opcionMenu=input("Ingresa la opcion: ")
        if opcionMenu == '1':
            cursor = collection_currency.find()
            for al in cursor:
                print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
            input("Presiona enter para continuar...")
        if opcionMenu == '2':
            print("1.location   2.screen_name  3.user_id")
            opcionMenu = input("Ingresa la opcion del atributo que quieras buscar: ")
            if opcionMenu == '1':
                a = input("Ingresa la locacion a buscar: ")
                cursor = collection_currency.find({"location":a})
                for al in cursor:
                    print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
                input("\nPresiona enter para continuar...")

            if opcionMenu == '2':
                a = input("Ingresa el screen_name a buscar: ")
                cursor = collection_currency.find({"screen_name":a})
                for al in cursor:
                    print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
                input("\nPresiona enter para continuar...")

            if opcionMenu == '3':
                a = int(input("Ingresa el user_id a buscar: "))
                cursor = collection_currency.find({"user_id":a})
                for al in cursor:
                    print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
                input("\nPresiona enter para continuar...")
        
    elif opcionMenu=="2":
        print ("Insertar Documento: \n")
        cursor = collection_currency.find()
        for al in cursor:
            print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
        print("\n")
        a = int(input("user_id: "))
        b = input("screen_name: " )
        c = input("location: ")
        d = int(input("followers_count: "))
        e = int(input("friends_count: "))
        collection_currency.insert_one({"user_id":a,"screen_name":b,"location":c,"followers_count":d, "friends_count":e})
        print("\n")
        cursor = collection_currency.find()
        for al in cursor:
            print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
        input("\nPresiona enter para continuar...")
        
    elif opcionMenu=="3":
        print ("Actualizacion de datos: \n")
        print ("Para actualizar el valor necesitas el user_id de alguien para editarlo.\n")
        print("Los valores a cambiar son los siguientes: \n")
        print("\t 1-screen_name  2-location  3-followers_count  4-friends_count\n")
        
        cursor = collection_currency.find()
        for al in cursor:
            print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
        print("\n")
        opcionMenu = input("Ingresa clave - valor a actualizar: ")

        if opcionMenu=='1':
               b = int(input("ingresa el user_id para cambiar el valor: "))
               a = input("Ingresa el nuevo screen_name: ")
               collection_currency.update_one({"user_id":b},{"$set":{"screen_name":a}})
               print ("\n")
               cursor = collection_currency.find()
               for al in cursor:
                   print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
               input("\nPresiona enter para continuar...")  
        if opcionMenu=='2':
               b = int(input("ingresa el user_id para cambiar el valor: "))
               a = input("Ingresa la nueva location: ")
               collection_currency.update_one({"user_id":b},{"$set":{"location":a}})
               print ("\n")
               cursor = collection_currency.find()
               for al in cursor:
                   print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
               input("\nPresiona enter para continuar...") 
        if opcionMenu=='3':
               b = int(input("ingresa el user_id para cambiar el valor: "))
               a = int(input("Ingresa el nuevo followers_count: "))
               collection_currency.update_one({"user_id":b},{"$set":{"followers_count":a}})
               print ("\n")
               cursor = collection_currency.find()
               for al in cursor:
                   print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
               input("\nPresiona enter para continuar...") 
        if opcionMenu=='4':
               b = int(input("ingresa el user_id para cambiar el valor: "))
               a = int(input("Ingresa el nuevo friends_count: "))
               collection_currency.update_one({"user_id":b},{"$set":{"friends_count":a}})
               print ("\n")
               cursor = collection_currency.find()
               for al in cursor:
                   print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
               input("\nPresiona enter para continuar...") 
                                  
    
    elif opcionMenu=="4":
        print ("Eliminacion de un Documento: \n")
        cursor = collection_currency.find()
        for al in cursor:
            print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
        print("\n")
        a = int(input("Ingresa el user_id para eliminar el documento deseado: "))
        collection_currency.delete_one({"user_id":a})
        print ("\n")
        cursor = collection_currency.find()
        for al in cursor:
            print("%i - %s - %s - %i - %i"  %(al['user_id'], al['screen_name'],al['location'],al['followers_count'],al['friends_count']))
        input("\nPresiona enter para continuar...")
        
    elif opcionMenu=="5":
        print("Hasta luego......")
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
