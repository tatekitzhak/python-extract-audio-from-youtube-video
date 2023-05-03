import pymongo
from pymongo import MongoClient
from pymongo.collation import Collation
from bson import ObjectId
import sys
from db.database_connection import db_connect
import db.collections.check_collection_exist as mymodule
import db.collections.insert as insert_module
import services.find_subcategory_name as services_module

if __name__ == "__main__":

    # Get the database db_connect (client)
    client = db_connect()
    if client != None:
        # the list_database_names() method returns a list of strings
        database_names = client.list_database_names()

        print("The client's list_database_names() method returned",len(database_names), "databases.")

        db = client["contxt"]
        collection = db["categories"]
        pipeline = [{'$lookup': {'from': 'subcategories',
                                 'localField': 'subcategories',
                                 'foreignField': '_id',
                                 'as': 'lookup_subcategories'
                                 }
                     }]
        doc = {
            'fname': 'Maayan',
            'lname': 'Itzhak',
            'fatherName': 'Ran',
            'matherName': 'Rachele',
            'age': 1.4,
            'gender': 'female'
        }
        services_module.get_collection("contxt", "categories", pipeline)
        # insert_module.insert_one(client, "mydatabase", "maayan4", doc)
        # insert_module.insert_many()
        # mymodule.collection_is_exist(client, 'sample_db', 'col-9')
        """db_is_exist(client, 'sample_db')"""
     #    msg = create_collection(client, 'sample_db', 'col-13')
     #    print('create_collection:',msg)
    else:
        print("The domain and port parameters passed to client's host is invalid")


"""
pipeline = [{'$lookup':{ 'from' : 'subcategories',
                                'localField' : 'subcategories',
                                'foreignField' : '_id',
                                'as' : 'lookup_categories'
                            }
                    }]
       print(client['contxt'].aggregate([{'$lookup':{ 'from' : 'subcategories',
                                'localField' : 'subcategories',
                                'foreignField' : '_id',
                                'as' : 'lookup_categories'
                            }
                    }]))
"""
