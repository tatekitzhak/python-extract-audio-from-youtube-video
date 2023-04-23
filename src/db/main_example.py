import pymongo
from pymongo import MongoClient
import json


def create_collection(client, db_name, col_name):
    db = client[db_name]
    collection = db[col_name]

    student = {
        'name': 'Maayan',
        'age': 1,
        'gender': 'female'
    }
    collection.insert_one(student)

    print('create_collection:', client.list_database_names())


def get_db_client():

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    db_client = MongoClient("mongodb://localhost:27017/")

    # Available databases
    print('datebases:', db_client.list_database_names())

    # Available collections in a specific database
    # db_information = dict((db, [collection for collection in db_client[db].list_collection_names()])
    #    for db in db_client.list_database_names())
    # print('databases information:',db_information)

    return db_client


if __name__ == "__main__":

    # Get the databases client
    dbs_client = get_db_client()
    create_collection(dbs_client, 'mydatabase', "maayan3")

    # Select database by name
    db = dbs_client['contxt']
    print('myDB:', db)
    # Available collections in a specific database
    print("collections:", db.list_collection_names())

    collection = db['categories']

    for document in collection.find():
        print("document: ", document)


{'_id': ObjectId('63ebec3e4c4c937143b210da'), 'name': 'RAN 1', 'tags': [], 'subcategories': [ObjectId('63ebec3e4c4c937143b210b4'), ObjectId('63ebec3e4c4c937143b210b5'), ObjectId('63ebec3e4c4c937143b210b6')], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 206000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 206000), 'lookup_categories': [{'_id': ObjectId('63ebec3e4c4c937143b210b4'), 'name': '111111111', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000),
                                                                                                                                                                                                                                                                                                                                                                       'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}, {'_id': ObjectId('63ebec3e4c4c937143b210b5'), 'name': '222222222', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}, {'_id': ObjectId('63ebec3e4c4c937143b210b6'), 'name': '333333333', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}]}
{'_id': ObjectId('63ebec3e4c4c937143b210df'), 'name': 'RAN 3', 'tags': [], 'subcategories': [ObjectId('63ebec3e4c4c937143b210ba'), ObjectId('63ebec3e4c4c937143b210bb'), ObjectId('63ebec3e4c4c937143b210bc')], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 210000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 210000), 'lookup_categories': [{'_id': ObjectId('63ebec3e4c4c937143b210bc'), 'name': 'CCCCCCCCCCC', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000),
                                                                                                                                                                                                                                                                                                                                                                            'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}, {'_id': ObjectId('63ebec3e4c4c937143b210ba'), 'name': 'AAAAAAAAAAA', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}, {'_id': ObjectId('63ebec3e4c4c937143b210bb'), 'name': 'BBBBBBBBBBB', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 184000)}]}
{'_id': ObjectId('63ebec3e4c4c937143b210fc'), 'name': 'RAN 2', 'tags': [], 'subcategories': [ObjectId('63ebec3e4c4c937143b210ca'), ObjectId('63ebec3e4c4c937143b210cb'), ObjectId('63ebec3e4c4c937143b210cc')], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 225000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 225000), 'lookup_categories': [{'_id': ObjectId('63ebec3e4c4c937143b210ca'), 'name': 'aaaaaa', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 195000),
                                                                                                                                                                                                                                                                                                                                                                            'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 195000)}, {'_id': ObjectId('63ebec3e4c4c937143b210cb'), 'name': 'bbbbbb', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 196000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 196000)}, {'_id': ObjectId('63ebec3e4c4c937143b210cc'), 'name': 'cccccc', 'tags': [], 'categories': [], 'topics': [], 'createdAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 196000), 'updatedAt': datetime.datetime(2023, 2, 14, 20, 17, 2, 196000)}]}
