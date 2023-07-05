import pymongo
from pymongo import errors

def insert_one(client, db_name, col_name, doc):
    db = client[db_name]
    collection = db[col_name]

    insert_res_info = collection.insert_one(doc)
    print('insert_one result:', insert_res_info)
    return insert_res_info

def add_one(client, db_name, col_name, doc):
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
    
        print (col_name, "has", col_dict['nrecords'], "documents on it.\n")
        return insert_res_info.inserted_id
    except errors.OperationFailure as err:
        col_dict = None
        print ("PyMongo ERROR:", err, "\n")
        return False

def add_many(client, db_name, col_name, doc):
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
    
        print (col_name, "has", col_dict['nrecords'], "documents on it.\n")
        return insert_res_info.inserted_id
    except errors.OperationFailure as err:
        col_dict = None
        print ("PyMongo ERROR:", err, "\n")
        return False

def aggregate_lookup_find_subcategory_name(client, db_name, col_name, pipeline):
    # https://github.com/mongomock/mongomock/blob/develop/tests/test__collection_api.py
    # https://stackoverflow.com/questions/48518215/mongodb-aggregation-lookup-with-conditions
    # https://gist.github.com/bertrandmartel/311dbe17c2a57e8a07610724310bf898
    # https://gist.github.com/umidjons/39469865d16b67bdfbea82ce85e11188
    # https://gist.github.com/trojanh/ce1b1ff579851e98ca29832e19672f3b
    
    """
    list_of_collections = db.list_collection_names()  # Return a list of collections in (client[db_name])

    if col_name in list_of_collections:  # Check if collection [col_name] exists in db (client[db_name])
        print("The collection exists.") 
    else:     
        print("The collection does not exist.")
    """

    try:
        db = client[db_name]
        col_dict = db.validate_collection(col_name)

        db = client[db_name]
        collection = db[col_name]

        aggregate_res = collection.aggregate(pipeline)
        print('aggregate_res:', aggregate_res)
    
        print (col_name, "has", col_dict['nrecords'], "documents on it.\n")
        return True
    except errors.OperationFailure as err:
        col_dict = None
        print ("PyMongo ERROR:", err, "\n")
        return False

"""
def update(id):
	user = mongo.db.users
	form = AddForm()
	if form.validate_on_submit():
		result = user.update({'_id':ObjectId(id)},{'$set':{'name':form.name.data, 'language': form.language.data}})
	return render_template("update.html",id=id,form=form)

    db['users'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    "name":name,
                    "age":age
                }
            }
        )

 def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)

"""