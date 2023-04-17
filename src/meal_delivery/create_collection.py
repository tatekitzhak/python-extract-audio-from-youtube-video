import json
# import the Collation module for PyMongo
from pymongo.collation import Collation
# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/

def check_existence_DB(db_name, client):
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
        print(f"'{db_name}' exists")
        return client[db_name]

    print(f" '{db_name}' does not exist")
    client = None
    return client
    

def check_existence_collection(client, db_name, col_name):

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

# def insert(col, doc_or_docs):

# Now let’s try to create a database and a collection.
"""
dataBase = client["exampleDB"]
check_existence_DB("exampleDB", client)
collection = dataBase["ExampleCollection"]
check_existence_collection("ExampleCollection", "exampleDB" , client)
"""
# Output
# 'exampleDB' does not exist
# Collection: 'ExampleCollection' in Database: 'exampleDB' does not exists

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
    db_is_exists = check_existence_DB(db_name, client)
    col_is_exists = check_existence_collection(client, db_name, col_name)

    if((db_is_exists != None) & (col_is_exists == None)):
        print('db_is_exists and col_not_exists:',db_is_exists)
        db.create_collection(
        name=col_name,
        codec_options=None,
        read_preference=None,
        write_concern=None,
        read_concern=None,
        session=None
        )
        col_dict = db.validate_collection(col_name)
        print(db.list_collection_names(), col_dict)
        #  raise TypeError("name_or_collection must be an instance of str or Collection")
        return 'A New Collection is created: ' + col_name
    else:
        
        return 'Database: ' + db_name + ' does not exist or collection: '+ col_name +' is exist'
    
    
   # create weekly demand collection
    # db.create_collection("weekly_demand")

    # create meal_info collection
    # db.create_collection("meal_info")

    print('list_collection_names:',db.list_collection_names())
    # get collection weekly_demand
    weekly_demand_collection = db.get_collection("weekly_demand")

    # open the weekly_demand json file
    with open("weekly_demand.json") as f:
        file_data = json.load(f)
        # print('file_data:',file_data)
    # insert the data into the collection
    # weekly_demand_collection.insert_many(file_data)
    print(weekly_demand_collection.find_one())

    # get the count of total data points
    """
    for document in weekly_demand_collection.find():
        print('weekly_demand_collection:',document)
    """