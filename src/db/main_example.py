import pymongo
from pymongo import MongoClient
import json

def create_collection(client, db_name, col_name):
   db = client[db_name]
   collection = db[col_name]

   student = {
      'name': 'Maayan',
      'age': 1,
      'gender': 'female'
   }
   collection.insert_one(student)

   print('create_collection:',client.list_database_names())


def get_db_client():
  
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   db_client = MongoClient("mongodb://localhost:27017/")

   # Available databases 
   print('datebases:',db_client.list_database_names())

   # Available collections in a specific database
   # db_information = dict((db, [collection for collection in db_client[db].list_collection_names()]) 
   #    for db in db_client.list_database_names())
   # print('databases information:',db_information)
 
   return db_client
  
if __name__ == "__main__":   
  
   # Get the databases client
   dbs_client = get_db_client()
   create_collection(dbs_client, 'mydatabase', "maayan3")
   
   # Select database by name
   db = dbs_client['contxt']
   print('myDB:', db)
   # Available collections in a specific database
   print ("collections:", db.list_collection_names())
  
   collection = db['categories']

   for document in collection.find():
       print("document: ", document)
   
   