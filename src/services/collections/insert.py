def insert_one(client, db_name, col_name, doc):
    db = client[db_name]
    collection = db[col_name]

    insert_res_info = collection.insert_one(doc)
    print('insert_one result:', insert_res_info)
    return insert_res_info


def insert_many(item='Item'):
    print('insert_many:', item)