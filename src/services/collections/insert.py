def insert_one(client, db_name, col_name, doc):
    db = client[db_name]
    collection = db[col_name]
    
    insert_result = collection.insert_one(doc)
    print('insert_one result:', insert_result.acknowledged)
    return insert_result.acknowledged

def insert_many(item='Item'):
    print('insert_many:', item)