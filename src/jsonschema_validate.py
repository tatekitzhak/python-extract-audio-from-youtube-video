import os
import json
import jsonschema
from jsonschema import validate

def validateJson(jsonData):
    schema_dir_path = os.getcwd() + '/schema/'
    with open(schema_dir_path + 'topic.json', 'r') as file:
        json_object = json.load(file)

    # Describe what kind of json you expect.
    json_schema = {
        "collMod": "product",
        "validator": {
            "$jsonSchema": json_object
            },
        "validationLevel": "strict",
        "validationAction": "error"
    }

    print('json_object:', json.dumps(json_schema, indent=2) )
    
    try:
        validate(instance=jsonData, schema=json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


# Convert json to python object (InValid).
jsonData = json.loads('{"name": "jane doe", "rollnumber": "25", "marks": 72}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print('Given JSON data is Valid:', jsonData)
else:
    print('Given JSON data is InValid:', jsonData)


"""
path_to_json = 'schema/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)  # for me this prints ['foo.json']

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)
    print(path_to_json , file_name)
"""
