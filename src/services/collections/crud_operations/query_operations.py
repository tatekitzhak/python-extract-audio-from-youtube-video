import sys, os, logging
import pymongo
from pymongo import errors
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))
from logger_track import events_logger

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'db')))
from db.database_connection import db_connect

def insert_one(client, db_name, col_name, doc):
    db = client[db_name]
    collection = db[col_name]

    insert_res_info = collection.insert_one(doc)
    print('insert_one result:', insert_res_info)
    return insert_res_info

def add_many(client, db_name, col_name, doc):
    """
    db_connect()
    client = db_connect()
    if client != None:
        print('ab:', client)
    """
    db = client[db_name]

    # list_of_collections = db.list_collection_names()  # Return a list of collections in (client[db_name])

    # if col_name in list_of_collections:  # Check if collection [col_name] exists in db (client[db_name])
    #     print("The collection exists.")
    # else:
    #     print("The collection does not exist.")

    try:
        col_dict = db.validate_collection(col_name)

        collection = db[col_name]

        insert_res_info = collection.insert_one(doc)
        print('insert_one result:', insert_res_info)

        print(col_name, "has", col_dict['nrecords'], "documents on it.\n")
        return insert_res_info.inserted_id
    except errors.OperationFailure as err:
        col_dict = None
        print("PyMongo ERROR:", err, "\n")
        return False


def aggregate_lookup_find_subcategory_name(db_name, col_name, pipeline):
    # https://github.com/mongomock/mongomock/blob/develop/tests/test__collection_api.py
    # https://stackoverflow.com/questions/48518215/mongodb-aggregation-lookup-with-conditions
    # https://gist.github.com/bertrandmartel/311dbe17c2a57e8a07610724310bf898
    # https://gist.github.com/umidjons/39469865d16b67bdfbea82ce85e11188
    # https://gist.github.com/trojanh/ce1b1ff579851e98ca29832e19672f3b

    client = db_connect()
    if client != None:

        try:
            db = client[db_name]
            col_dict = db.validate_collection(col_name)

            collection = db[col_name]

            aggregate_res = collection.aggregate(pipeline)

            print(col_name, "has", col_dict['nrecords'], "documents on it.\n")
            return aggregate_res
        except errors.OperationFailure as err:
            
            print("PyMongo ERROR:", err, "\n")
            events_logger(__name__, f" {err}", logging.ERROR, logging.DEBUG)
            return False


def update_ref_ids(db_name: str, col_name: str, _id: str, new_id: str, ids = [] ) -> dict:

    client = db_connect()
    if client != None:
        db = client[db_name]

        try:
            col_dict = db.validate_collection(col_name)

            # Update multy array

            # result = db[col_name].find_one_and_update(
            #     {'_id': ObjectId(_id)},
            #     { 
            #     '$addToSet': { 
            #         'topic_ref_ids': {
            #             '$each': ids
            #             }
            #         } 
            #     },
            #     return_document=ReturnDocument.AFTER
            # )

            # Update singale item

            # result = db[col_name].update_one({'_id': ObjectId(_id)}, {
            #                             '$addToSet': {"topic_ref_ids": new_id}}, upsert=True)
                                        
            result = db[col_name].find_one_and_update(
                {'_id': ObjectId(_id)}, 
                {
                    '$addToSet': {
                        "topic_ref_ids": ObjectId(new_id)
                        }
                }, 
                return_document=ReturnDocument.AFTER )

            print(col_name, "has", col_dict['nrecords'], "documents on it.\n", "ReturnDocument.AFTER:", result)
            return result
        except errors.OperationFailure as err:
            col_dict = None
            print("PyMongo ERROR:", err, "\n")
            events_logger(__name__, f" {err}", logging.ERROR, logging.DEBUG)
            return False

def add_one(db_name: str, col_name: str, new_doc: dict, id_ref='') -> str:
    # print(db_name, col_name, new_doc)
    client = db_connect()
    if client != None:
        db = client[db_name]

        try:
            col_dict = db.validate_collection(col_name)

            collection = db[col_name]

            insert_res_info = collection.insert_one(new_doc)
            print('insert_one result:', insert_res_info)

            print("Before insert, ",col_name, "has", col_dict['nrecords'], "documents on it.\n")
            if isinstance(insert_res_info.inserted_id, ObjectId) and id_ref:
                print('ObjectId:', ObjectId(insert_res_info.inserted_id), type(ObjectId))
                # update_ref_ids(db_name, col_name, id_ref, new_id) 
            return insert_res_info
        except errors.OperationFailure as err:
            events_logger(__name__, f"{err}", logging.ERROR, logging.DEBUG)
            return False

    


"""
 def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)

"""
