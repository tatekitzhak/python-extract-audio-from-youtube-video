import pymongo
from pymongo import MongoClient
import json

def create_db_collection(client):
   db = client['mydatabase']
   collection = db["person1"]

   student = {
      'name': 'Maayan',
      'age': 1,
      'gender': 'female'
   }
   collection.insert_one(student)

   print('create_db_collection:',client.list_database_names())


def get_database():
  
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   db_client = MongoClient("mongodb://localhost:27017/")

   # Available databases 
   print('datebases:',db_client.list_database_names())

   # Available collections in a specific database
   d = dict((db, [collection for collection in db_client[db].list_collection_names()]) 
      for db in db_client.list_database_names())
   print('json.dumps(d):',d['contxt'])
 
   return db_client
  
if __name__ == "__main__":   
  
   # Get the database
   mydatabase = get_database()
   create_db_collection(mydatabase)
   
   # Select database by name
   db = mydatabase['contxt']
   print('myDB:', db)
   # Available collections in a specific database
   print ("collections:", db.list_collection_names())
  
   collection = db['categories']

   for document in collection.find():
       print(document)
   
   