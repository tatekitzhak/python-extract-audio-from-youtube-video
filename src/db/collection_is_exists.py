"""
CheckDatabaseExists
"""
from pymongo.collation import Collation
# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/

def check_collection_exists(client, db_name, col_name):
    
    #  It verifies the existence of collection name in a database
    db = client[db_name]
    col_list = db.list_collection_names()
    # col_dict = db.validate_collection(col_name)
    if col_name in col_list:
        print(f"Collection: '{col_name}' in Database: '{db_name}' exists", col_list)
        return col_name
    else:
        print(f"Collection: '{col_name}' in Database: '{db_name}' does not exists") 
        return None