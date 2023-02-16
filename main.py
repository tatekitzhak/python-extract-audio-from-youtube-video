# import convert_tuple_into_json
import mysql_connection
import create_folder

def main():
	topics_data = mysql_connection.main()
	print('Response processing module:', create_folder.main(topics_data))


main()