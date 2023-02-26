import pymongo
from pymongo import MongoClient
import sys
from create_collection import create_collection

sys.path.append('../db' )
from database_connection import db_connect


  
if __name__ == "__main__":   
  
   # Get the database db_connect
   client = db_connect()
   if client != None:
       # the list_database_names() method returns a list of strings
       database_names = client.list_database_names()

       print("The client's list_database_names() method returned", len(database_names), "database names.")
       msg = create_collection(client, 'sample_db', 'col-8')
       print(msg)
   else:
       print("The domain and port parameters passed to client's host is invalid")
   
   
   