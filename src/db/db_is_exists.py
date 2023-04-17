"""
CheckDatabaseExists
"""
from pymongo.collation import Collation
# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/

def check_db_exists(db_name, client):
    # the list_database_names() method returns a list of strings
    list_of_dbs = client.list_database_names()
    
    for col_num, db in enumerate(list_of_dbs):
        # print ("\nGetting collections for database:", db, "--", col_num)
        # Return collection names
        collection_names = client[db].list_collection_names()
        print ("The MongoDB database returned", len(collection_names), "collections.", collection_names)

        # iterate over the list of collection names
        for col_num, col in enumerate(collection_names):
            print ('#col name:', col, ", index:", col_num)
   
    # It verifies the existence of DB
    if db_name in list_of_dbs:
        print(f"'{db_name}' isExist")
        return client[db_name]

    print(f" '{db_name}' does not exist")
    client = None
    return client