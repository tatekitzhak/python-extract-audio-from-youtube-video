import mysql.connector
from mysql.connector import Error
import os, errno
import json
import re

ROOT_DIR  = os.path.dirname(os.path.abspath(__file__))

def convert_tuple_to_json(tup, obj):
    for a, b,c,d in tup:
        # print ('a:', a)
        # print ('b:', b)
        # print ('b:', c)
        # print ('b:', d)
        obj.setdefault(b, []).append(c)
    return obj

def filter_non_alphanumeric_char(topic):

    # Remove all non-word characters (everything except numbers and letters)
    topic = re.sub(r"[^\w\s]", '', topic)

    # Remove all end of string non alphanumeric characters (i.e: question mark or space)
    topic = re.sub(r"[\s|\?]+$", '', topic)

    # Replace all runs of whitespace with a single dash
    topic = re.sub(r"\s+", '-', topic)

    return topic

def create_folder(topic_name, subtopic_name):
    if topic_name and subtopic_name:
        path= ROOT_DIR+'/'+topic_name+'/'+subtopic_name
        print(path)
    else:
        path= ROOT_DIR+'/'+topic_name
        print(path)

    # path= ROOT_DIR+'/'+topic_name

    # Check whether the specified path exists or not
    path_isExist = os.path.exists(path)
    print('IsExis a tpath : ',path_isExist)

    if not path_isExist:
      
      # Create a new directory because it does not exist 
        try:
            os.makedirs(path)
            print("The new directory is created =>", topic_name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

def main(topics_data):

    json_dictionary = {}

    data_obj = convert_tuple_to_json(topics_data, json_dictionary)

    # Create a new topics directory
    for topic in data_obj:
        topic_name = filter_non_alphanumeric_char(topic)
        create_folder(topic_name, None)
        print(topic_name,":")

        # Create a new subtopics directory
        for subtopic in json_dictionary[topic]:
            try:
                subtopic_name = filter_non_alphanumeric_char(subtopic)
                create_folder(topic_name,subtopic_name)
                print(subtopic_name)
            except Exception as e:
                raise
            else:
                pass
            finally:
                pass
    return __name__

# main([("apple", "banana", "cherry")])

# def create_folders():
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='db_test1',
#                                              user='ran',
#                                              password='ran')
#         if connection.is_connected():
#             db_Info = connection.get_server_info()
#             print("Connected to MySQL Server version ", db_Info)
            
#         query = "select * from topics"
#         cursor = connection.cursor()
#         cursor.execute(query)
#         # get all records
#         records = cursor.fetchall()
#         print("Total number of rows in table: ", cursor.rowcount)

#         print("\n Table data: ",records)
#         for row in records:
#             # print("Rows = ", row[1] )
#             # create_topics_folders(row[1])
#             print('__________________')

#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")

# create_folders()
