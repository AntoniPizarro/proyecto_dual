#https://www.youtube.com/watch?v=VQnmcBnguPY&t=803s
from pymongo import MongoClient

def insertarUno(nave):
    cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/?retryWrites=true&w=majority')
    db = cliente['proyecto_dual']
    #nave = {'modelo':modelo,'marca':marca,'gama':gama,'tasa':tasa,'color':color,'plazas':plazas,'caracteristicas':caracteristicas}
    doc = {'modelo':nave['modelo'],'marca':nave['marca'],'gama':nave['gama'], 'tasa':nave['tasa'], 'color':nave['color'], 'plazas':nave['plazas'], 'caracteristicas':nave['caracteristicas']}
    db.datos_naves.insert_one(doc)