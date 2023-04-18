import pymongo
from pymongo import MongoClient
from bson import ObjectId
import sys
sys.path.append('db')

from database_connection import db_connect

mongo_client = db_connect()

db = mongo_client["sample_db"]
col = db["weekly_demand"]
print('INDEX')

# cursor = col.find({})
# for document in cursor:
#     print(document)

col.update_one({'_id':ObjectId("63f4c294eac3552f917ab06c")}, {"$set": {"meal_id" : 1122337778}}, upsert=False)
print(col.find_one(
        ObjectId("63f4c294eac3552f917ab06c")
    ))