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
       
       db = client[db_name]
       collection = db[coll]
       for doc in collection.aggregate(pipeline):
        #    print("subcategories _ids:",doc['subcategories'])
           for subcat_id in doc['subcategories']:
            #    print('subcat_id:', subcat_id)
               for sub_doc in doc['lookup_subcategories']:
                   if subcat_id == sub_doc['_id']:
                    #    if _ids match call youtube procsess
                       print(f"Categorie name: '{doc['name']}', Subcategorie name: '{sub_doc['name']}, _id: '{sub_doc['_id']}'")
                   else:
                       print(f"ERROR, DATA NOT MATCH: Categorie name: '{doc['name']}', Subcategorie name: '{sub_doc['name']}, _id: '{sub_doc['_id']}'")
       return collection

   else:
       print(f"One of them is invalid: '{db_name}', '{coll}', '{pipeline}' ")
    

