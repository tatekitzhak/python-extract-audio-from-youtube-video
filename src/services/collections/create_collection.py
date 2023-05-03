import json
# import the Collation module for PyMongo
from pymongo.collation import Collation
from check_db_exist import db_is_exist
from check_collection_exist import collection_is_exist

# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/


def create_collection(client, db_name, col_name):
    """ 
    # create a collation object for the new collection
colla = Collation(
locale = "en_US",
strength = 2,
numericOrdering = True,
backwards = False
)

# dictionary version of the same collation
# colla = {'locale': 'en_US', 'strength': 2, 'numericOrdering': True, 'backwards': False}

    try:
        col = db.create_collection(
        name=collection_name,
        codec_options=None,
        read_preference=None,
        write_concern=None,
        read_concern=None,
        session=None,
        collation=colla
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
    col_is_exist_ = collection_is_exist(client, db_name, col_name)

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