import sys
import pymongo
from pymongo import MongoClient
from pymongo.collation import Collation
sys.path.append('./db')
from db.database_connection import db_connect
# from services.collections.create_collection import create_collection_with_validation_rules
import services.collections.create_collection as create_collection
from services.collections.check_collection_exist import collection_is_exist
# Lookup Aggregations:
""" 
https://hevodata.com/learn/mongodb-lookup/
https://stackoverflow.com/questions/41992885/pymongo-how-to-match-on-lookup
"""

def handle_topic(subcategory_name):

    client = db_connect()

    # collection_is_exist(client, "sample_db", "topic_schema4")
    if client != None:
        res = create_collection.create_collection_with_collMod_method_2(client, 'sample_db', 'article','')
        print('handle_topic:', res)

def find_subcategory_name(db_name, coll, pipeline):   
   handle_topic('abc')
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
                    #    if _ids match call youtube procsess by Subcategorie name
                       print(f"Categorie name: '{doc['name']}', Subcategorie name: ")
                   else:
                       print(f"ERROR, DATA NOT MATCH: Categorie name: '{doc['name']}', Subcategorie name: '{sub_doc['name']}, _id: '{sub_doc['_id']}'")
       return collection

   else:
       print(f"One of them is invalid: '{db_name}', '{coll}', '{pipeline}' ")
    

