#Enlace a un video que explica como funciona pymongo
#https://www.youtube.com/watch?v=VQnmcBnguPY&t=803s

#Importación de librerías
from pymongo import MongoClient
from pprint import pprint

#Función principal
def insertarUno(nave):
    #Conexión al cluster de mongo
    cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/?retryWrites=true&w=majority')
    #Selección de la base de datos
    db = cliente['proyecto_dual']
    #Esquema del diccionario con los datos a introducir en la base de datos:
    #nave = {'modelo':modelo,'marca':marca,'gama':gama,'tasa':tasa,'color':color,'plazas':plazas,'caracteristicas':caracteristicas}
    doc = {'modelo':nave['modelo'],'marca':nave['marca'],'gama':nave['gama'], 'tasa':nave['tasa'], 'color':nave['color'], 'plazas':nave['plazas'], 'caracteristicas':nave['caracteristicas']}
    #Variable de comprobación
    compr = {'modelo':doc['modelo']}
    #Se guardan todos los documentos encontrados en mongo que coincidan con la variable de comprobación
    #Esto evitara que existan dos documentos que hagan referencia al mismo servicio
    documentos = db.datos_naves.find(compr)
    #Se comprueban existencias coincidentes
    if documentos.count() == 0:
        #Si no existe ningún documento igual, lo genera
        db.datos_naves.insert_one(doc)
        print(" ")
        print("Servicio guardado:")
        #Muestra el documento generado estructuradamente
        pprint(doc)
    else:
        #Si ya existe un documento, entonces actualiza el documento existente con los datos recogidos
        print(" ")
        print("Servicio actualizado:")
        db.datos_naves.update_one(compr,{"$set":doc})
        #Muestra el documento generado estructuradamente
        pprint(doc)