import os, sys, json, jsonschema, logging
from jsonschema import validate
import pymongo
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from pymongo.collation import Collation
from collections import OrderedDict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'db')))
from database_connection import db_connect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
from logger_track import events_logger

print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'db')))

# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/

def create_collection_with_validation_rules(client="", db_name="", collection_name="", json_schema=""):
    print("hello:",client, db_name, collection_name, json_schema)
    coll = Collation(
        locale = "en_US",
        strength = 2,
        numericOrdering = True,
        backwards = False
    )
    db = client[db_name]
    
    coll_create_result = db.create_collection(
        name=collection_name,
        validator={"$jsonSchema": json_schema},
        validationLevel= "strict",
        validationAction= "error",
        collation=coll
    )
    
    return coll_create_result

def create_collection_method_1(client="", db_name="", collection_name="", json_schema=""):

    db = client[db_name]
    
    try:
        collection_created = db.create_collection(collection_name)
        
        print('create_collection_method_1 :', collection_created)
        return collection_created
    except CollectionInvalid:
        raise CollectionInvalid("Collection %s already exists" % collection_name)
    
def create_collection_with_collMod_method_2(client="", db_name="", collection_name="", schema="") -> dict:

    db = client[db_name]
    schema_dir_path = os.getcwd() + '/schema/'
    with open(schema_dir_path + collection_name+'.json', 'r') as file:
        json_object = json.load(file)

    validator = {
            "$jsonSchema": json_object,
            # "validationLevel": "strict",
            # "validationAction": "error"
    }

    query = [('collMod', collection_name),('validator', validator)]
    try:
        coll_created_res = db.create_collection(collection_name)
        return coll_created_res
    except CollectionInvalid:
        # raise CollectionInvalid("collection %s already exists" % collection_name)
        pass
    command_result = db.command(OrderedDict(query))

    print('create_collection_with_collMod_method_2:', command_result)
    return command_result

def create_collection_with_collMod_command(db_name: str, collection_name: str) -> dict:
    # DIR1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

    # print('os.path.dirname(__file__):', DIR1)
    client = db_connect()
    if client != None:

        command_result = {}
        db = client[db_name]

        try:
            schema_dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'schema', collection_name+'.json'))
               
            with open(schema_dir_path, 'r') as file:
                json_object = json.load(file)

                validator = {
                        "$jsonSchema": json_object,
                        # "validationLevel": "strict",
                        # "validationAction": "error"
                }

                query = [('collMod', collection_name),('validator', validator)]
                try:
                    coll = Collation(locale = "en_US", strength = 2, numericOrdering = True, backwards = False)

                    create_coll = db.create_collection(
                        name=collection_name,
                        collation=coll
                    )
                    command_result = db.command(OrderedDict(query))

                except CollectionInvalid as e:
                    events_logger(__name__, f"Collection Invalid Errors: '{collection_name}' already exists. {e}", logging.ERROR, logging.DEBUG)
                    raise CollectionInvalid("collection %s already exists" % collection_name)
                else:
                    print(f"Collection '{collection_name}' successfully created")
        except FileNotFoundError as e:
            events_logger(__name__, f"FileNotFoundError: {e}", logging.ERROR, logging.DEBUG)
            raise e

        print('create_collection_with_collMod_command:', command_result)
        
        return {
            "message": "Collection status",
            "create_collection_result": create_coll,
            "command_collMod_result": command_result
        }

def create_collection(client, db_name, col_name):
    """ 
    # create a collation object for the new collection
coll = Collation(
locale = "en_US",
strength = 2,
numericOrdering = True,
backwards = False
)

# dictionary version of the same collation
# coll = {'locale': 'en_US', 'strength': 2, 'numericOrdering': True, 'backwards': False}

    try:
        col = db.create_collection(
        name=collection_name,
        codec_options=None,
        read_preference=None,
        write_concern=None,
        read_concern=None,
        session=None,
        collation=coll
        )
    except Exception as err:

        # collection already exists
        if "already exists" in err._message:
            col = db[collection_name]
        else:
            print ("create_collection() ERROR:", err)
            col = None

        print ("Collection name:", col.name)
    """
    