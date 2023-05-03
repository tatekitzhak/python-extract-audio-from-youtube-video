def insert_one(client, db_name, col_name, doc):
    db = client[db_name]
    collection = db[col_name]
    
    inserted_result = collection.insert_one(doc)
    print('inserted result:', inserted_result)
    return inserted_result

def insert_many(item='Item'):
    print('insert_many:', item)