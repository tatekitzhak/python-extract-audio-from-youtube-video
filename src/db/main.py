import pymongo
from pymongo import MongoClient
def get_database():
  
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   conn = MongoClient("mongodb://localhost:27017/")
   print('datebases:',conn.list_database_names())
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return conn.contxt
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   mydatabase = get_database()
   print ("mydatabase:", mydatabase.collection)
   collection = mydatabase.categories

   for document in collection.find():
       print(document['name'])
   
   