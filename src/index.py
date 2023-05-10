import pymongo
from pymongo import MongoClient
from pymongo.collation import Collation
from bson import ObjectId
import sys
from db.database_connection import db_connect
import db.collections.check_collection_exist as mymodule
import db.collections.insert as insert_module
import services.lookup_subcategories_data as subcategories_data

if __name__ == "__main__":

    # Get the database db_connect (client)
    client = db_connect()
    if client != None:
        # the list_database_names() method returns a list of strings
        database_names = client.list_database_names()

        print("The client's list_database_names() method returned",len(database_names), "databases.")

        db = client["contxt"]
        collection = db["categories"]
        pipeline = [{'$lookup': {'from': 'subcategories',
                                 'localField': 'subcategories',
                                 'foreignField': '_id',
                                 'as': 'lookup_subcategories'
                                 }
                     }]
        
        # subcategories_data.find_subcategory_name("contxt", "categories", pipeline)
        
        doc = {
            'fname': 'Maayan1',
            'lname': 'Itzhak1',
            'fatherName': 'Ran1',
            'matherName': 'Rachele1',
            'age': 1.4,
            'gender': 'female'
        }

        doc2 = { "name": "Alice2",
                 "year": 2018,
                 "major": "History",
                 "gpa": 3.2,
                 "address":{
                    "city": "NYC",
                    "street": "33rd Street"
                  }
        }

        doc3 = {
            'name': 'Mobile and Embedded Systems333',
            'title': 'CompTIA Security+ Guide to Network Security Fundamentals Module 5: Mobile, Embedded, & Spec. Devices',
            'description': 'Mobile, Embedded, & Spec. Devices',
            'video': {
                'url': 'https://www.youtube.com/watch?v=RtSI0T4rMjo'
            },
            'article': 'This article is contributed by Rishabh Bansal and Shaurya Uppal. If you like GeeksforGeeks and would like to contribute, you can also write an article using contribute.geeksforgeeks.org or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.',
            'rating': 1.433,
            'tags': '#Mobile. #Embedded. #Systems.'
        }
        insert_res_info = insert_module.insert_one(client, "sample_db", "topic_schema8", doc3)
        print('insert_res_info:',insert_res_info.inserted_id)
        # mymodule.collection_is_exist(client, 'sample_db', 'col-9')
        # db_is_exist(client, 'sample_db')
     #    msg = create_collection(client, 'sample_db', 'col-13')
     #    print('create_collection:',msg)
    else:
        print("The domain and port parameters passed to client's host is invalid")

"""

doc = {
            'name': 'Mobile and Embedded Systems',
            'title': 'CompTIA Security+ Guide to Network Security Fundamentals Module 5: Mobile, Embedded, & Spec. Devices',
            'description': 'Mobile, Embedded, & Spec. Devices',
            'article': 'This article is contributed by Rishabh Bansal and Shaurya Uppal. If you like GeeksforGeeks and would like to contribute, you can also write an article using contribute.geeksforgeeks.org or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.',
            'rating': 1.4,
            'tags': '#Mobile. #Embedded. #Systems.'
        }
        insert_res_info = insert_module.insert_one(client, "sample_db", "topic_schema9", doc)

"""