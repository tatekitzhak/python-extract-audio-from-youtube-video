import json
import re
import create_folder


def convert_tuple_to_json(tup, obj):
    for a, b,c,d in tup:
    	# print ('a:', a)
    	# print ('b:', b)
    	# print ('b:', c)
    	# print ('b:', d)
        obj.setdefault(b, []).append(c)
    return obj

def remove_replc_non_alphanumeric(str):

    # Remove all non-word characters (everything except numbers and letters)
    str = re.sub(r"[^\w\s]", '', str)

    # Remove all end of string non alphanumeric characters (i.e: question mark or space)
    str = re.sub(r"[\s|\?]+$", '', str)

    # Replace all runs of whitespace with a single dash
    str = re.sub(r"\s+", '-', str)

    return str

def main(topics_data):

	json_dictionary = {}

	data_obj = convert_tuple_to_json(topics_data, json_dictionary)

	# Create a new topics directory
	for topic in data_obj:
		topics = remove_replc_non_alphanumeric(topic)
		create_folder.create_topics_folders(topics)
		print(topics,":")

		# Create a new subtopics directory
		for subtopic in json_dictionary[topic]:
			try:
				subtopics = remove_replc_non_alphanumeric(subtopic)
				create_folder.create_subtopics_folders(topics,subtopics)
				print(subtopics)
			except Exception as e:
				raise
			else:
				pass
			finally:
				pass
	return __name__





