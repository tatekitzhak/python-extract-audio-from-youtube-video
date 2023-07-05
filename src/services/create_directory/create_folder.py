import os, errno
import json
import re

# DIR1 = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..', 'converted_audio'))

def filter_non_alphanumeric_char(topic: str) -> str:

    # Remove all non-word characters without a hyphen (everything except numbers and letters)
    topic = re.sub(r"[^\w\s\-]", '', topic)

    # Remove all end of string non alphanumeric characters (i.e: question mark or space)
    topic = re.sub(r"[\s|\?]+$", '', topic)

    # Replace all runs of whitespace with a single dash
    topic = re.sub(r"\s+", '-', topic)

    return topic

def create_folder(category_name: str, subcategory_name: str) -> str:

    category = filter_non_alphanumeric_char(category_name)
    subcategory = filter_non_alphanumeric_char(subcategory_name)
   
    DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../..', 'converted_audio', category, subcategory))

    path_is_exist = os.path.exists(DIR)
    print('path IsExis : ',path_is_exist)

    if not path_is_exist:
      
      # Create a new directory because does not exist 
        try:
            os.makedirs(DIR)
            print("The new directory is created: ", DIR)
            return DIR
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else :
        return DIR

