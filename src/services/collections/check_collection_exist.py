"""
Check if Database Exists
"""
from pymongo.collation import Collation
# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/

def collection_is_exist(client, db_name, col_name):
    
    #  It verifies the existence of collection name in a database
    db = client[db_name]
    coll_list = db.list_collection_names()
    # col_dict = db.validate_collection(col_name)
    if col_name in coll_list:
        print(f"Collection: '{col_name}' in database '{db_name}' is exists", client[db_name])
        return coll_list
    else:
        print(f"Collection: '{col_name}' in database '{db_name}' does not exists") 
        return None