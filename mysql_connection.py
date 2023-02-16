# https://bitworks.software/en/2019-03-12-tornado-persistent-mysql-connection-strategy.html
# https://stackoverflow.com/questions/66858012/how-to-share-a-mysql-connection-that-is-inside-a-function

import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector
from mysql.connector import Error

db_host = os.getenv("DBHOST")
db_name = os.getenv("DBNAME")
db_user = os.getenv("DBUSER")
db_password = os.getenv("DBPASS")


def init_db_connection(host_name, db_name, user_name, user_password):
	
    try:
        connection = mysql.connector.connect(
				            host=host_name,
				            database=db_name,
				            user=user_name,
				            passwd=user_password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connection to MySQL Server successful. version: ", db_Info)
        # print("Connection to MySQL DB successful")
    except Error as e:
        print("Error while connecting to MySQL:", e)
    return connection


def db_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # get all records
        records = cursor.fetchall()
        print("Database get all records successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed successfully")
    return records



def main():
	connection = init_db_connection(db_host, db_name, db_user, db_password)
	# queries
	if connection.is_connected():
		query = "SELECT tc.`id`, topic, subtopic, sc.`topic_id` FROM `topics` tc INNER JOIN `subtopics` sc ON tc.`id`= sc.`topic_id`"

		query2 = "SELECT * FROM subtopics"
		data = db_query(connection, query)
		# print("Database records: ", data)
	return data



