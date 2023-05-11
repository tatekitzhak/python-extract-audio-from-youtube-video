import os, sys, json, jsonschema
from jsonschema import validate
import pymongo
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
sys.path.append('../db')
from pymongo.collation import Collation
from collections import OrderedDict
from check_db_exist import db_is_exist
from services.collections.check_collection_exist import collection_is_exist

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
    
    # if collection not exist create the collection_name
    coll_is_exist = collection_is_exist(client, db_name, collection_name)
    if 0:
        print('create_collection_method_1 *:', coll_is_exist)
        return True
    else:
    
        try:
            coll_created_res = db.create_collection(collection_name)
            print('create_collection_method_1 **:', coll_created_res)
            return coll_created_res
        except CollectionInvalid:
            raise CollectionInvalid("collection %s already exists" % collection_name)

def create_collection_with_collMod_method_2(client="", db_name="", collection_name="", schema=""):

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
        db.create_collection(collection_name)
    except CollectionInvalid:
        # raise CollectionInvalid("collection %s already exists" % collection_name)
        pass
    command_result = db.command(OrderedDict(query))

    print('create_collection_with_collMod_method_2:', command_result)
    return command_result

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
    db = client[db_name]
    db_is_exist_ = db_is_exist(db_name, client)
    col_is_exist_ = check_collection_exist.collection_is_exist(client, db_name, col_name)

    if((db_is_exist_ != None) & (col_is_exist_ == None)):
        print('db_is_exist_ and col_not_exists:',db_is_exist_)
        db.create_collection(name=col_name, codec_options=None, read_preference=None, write_concern=None, read_concern=None, session=None)
        col_dict = db.validate_collection(col_name)
        print(db.list_collection_names(), col_dict)
        #  raise TypeError("name_or_collection must be an instance of str or Collection")
        return 'A New Collection is created: ' + col_name
    else:
        return 'Database: ' + db_name + ' does not exist or collection: '+ col_name +' is exist'

    print('list_collection_names:',db.list_collection_names())