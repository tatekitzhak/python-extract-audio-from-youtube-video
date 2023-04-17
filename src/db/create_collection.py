# https://analyticsindiamag.com/guide-to-pymongo-a-python-wrapper-for-mongodb/
def check_existence_DB(db_name, client):
     """It verifies the existence of DB"""
     list_of_dbs = client.list_database_names()
     if db_name in list_of_dbs:
         print(f"'{db_name}' exists")
     print(f" '{db_name}' does not exist")

def check_existence_collection(collection_name, db_name, client):
    """It verifies the existence of collection name in a database"""
    db = client[db_name]
    collection_list = db.list_collection_names()
    if collection_name in collection_list:
        print(f"Collection: '{collection_name}' in Database: '{db_name}' exists")
    print(f"Collection: '{collection_name}' in Database: '{db_name}' does not exists") 

# Now let’s try to create a database and a collection.

dataBase = client["exampleDB"]
check_existence_DB("exampleDB", client)
collection = dataBase["ExampleCollection"]
check_existence_collection("ExampleCollection", "exampleDB" , client)

# Output
# 'exampleDB' does not exist
# Collection: 'ExampleCollection' in Database: 'exampleDB' does not exists

def create_db_collection(client):
   db = client['mydatabase']
   collection = db["person1"]

   student = {
      'name': 'Maayan',
      'age': 1,
      'gender': 'female'
   }
   collection.insert_one(student)

   print('create_db_collection:',client.list_database_names())
