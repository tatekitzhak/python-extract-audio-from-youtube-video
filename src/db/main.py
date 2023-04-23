import pymongo
import sys
from pymongo import MongoClient
from database_connection import db_connect
from create_collection import create_collection
from collection.check_collection_exist import collection_is_exist
from check_db_exist import db_is_exist
sys.path.append('collection')
  
if __name__ == "__main__":   
  
   # Get the database db_connect (client)
   client = db_connect()
   if client != None:
       # the list_database_names() method returns a list of strings
       database_names = client.list_database_names()

       print("The client's list_database_names() method returned", len(database_names), "databases.")

       collection_is_exist(client, 'sample_db', 'col-9')
       """db_is_exist(client, 'sample_db')"""
    #    msg = create_collection(client, 'sample_db', 'col-13')
    #    print('create_collection:',msg)
   else:
       print("The domain and port parameters passed to client's host is invalid")
   
   
   