from pymongo import MongoClient

cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/accion?retryWrites=true&w=majority')
db = cliente['high_schools']
print(db.list_collection_names())