import sys
import pymongo
from pymongo import MongoClient
from pymongo.collation import Collation
sys.path.append('./db')
from db.database_connection import db_connect

"""
https://hevodata.com/learn/mongodb-lookup/
https://stackoverflow.com/questions/41992885/pymongo-how-to-match-on-lookup

"""
def get_collection(db_name, coll, pipeline):   
  
   # Get the database db_connect (client)
   client = db_connect()
   if client != None:
       # the list_database_names() method returns a list of strings
       database_names = client.list_database_names()
       
       db = client[db_name]
       collection = db[coll]

       for doc in collection.aggregate(pipeline):
           print("doc:", doc['lookup_categories'])
           for subdoc in doc['lookup_categories']:
               print('subcaterories:', subdoc['_id'])

   else:
       print(f"One of them is invalid: '{db_name}', '{coll}', '{pipeline}' ")
    

