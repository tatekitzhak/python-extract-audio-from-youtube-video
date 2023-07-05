import pymongo
from pymongo import MongoClient, errors


def db_connect():
    DOMAIN = 'localhost:'
    PORT = 27017
    try:
        # try to instantiate a client instance
        # db_client = MongoClient("mongodb://localhost:27017/")
        db_client = MongoClient(host=[str(DOMAIN) + str(PORT)],
                                serverSelectionTimeoutMS=3000  # 3 second timeout
                                )

        # print the version of MongoDB server if connection successful
        print("DB server version:", db_client.server_info()["version"])
        
        """
        # Get server information
        for k, v in db_client.server_info().items():
            print("Key: {} , Value: {}".format(k, v))

        # Get server status of admin database
        print("Server status {}".format(db_client.admin.command("serverStatus")))

        # List databases
        databases = db_client.list_database_names()
        print("Databases: {}".format(databases))
        """
        return db_client

    except errors.ServerSelectionTimeoutError as err:
        # set the client instance to 'None' if exception
        db_client = None

        # catch pymongo.errors.ServerSelectionTimeoutError
        print("pymongo ERROR, Server not available:", err)
        return db_client
