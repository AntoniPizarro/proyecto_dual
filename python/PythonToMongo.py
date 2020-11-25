#https://www.youtube.com/watch?v=VQnmcBnguPY&t=803s
from pymongo import MongoClient
from pprint import pprint

def insertarUno(nave):
    cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/?retryWrites=true&w=majority')
    db = cliente['proyecto_dual']
    #nave = {'modelo':modelo,'marca':marca,'gama':gama,'tasa':tasa,'color':color,'plazas':plazas,'caracteristicas':caracteristicas}
    doc = {'modelo':nave['modelo'],'marca':nave['marca'],'gama':nave['gama'], 'tasa':nave['tasa'], 'color':nave['color'], 'plazas':nave['plazas'], 'caracteristicas':nave['caracteristicas']}
    compr = {'modelo':doc['modelo']}
    documentos = db.datos_naves.find(compr)
    if documentos.count() == 0:
        db.datos_naves.insert_one(doc)
        print("Servicio guardado:")
        pprint(doc)
    else:
        print("Servicio actualizado:")
        db.datos_naves.update_one(compr,{"$set":doc})
        pprint(doc)

cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/accion?retryWrites=true&w=majority')
db = cliente['high_schools']
print(db.list_collection_names())
