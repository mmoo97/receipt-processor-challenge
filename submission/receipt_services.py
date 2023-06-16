import uuid
import json
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from openapi_schema_validator import validate

spec_dict, spec_url = read_from_filename('../api.yml')

validate_spec(spec_dict)

file = open('schema.json')

schema = json.load(file)

file.close()

in_mem_db = {}

def process_receipt(request):

    # print(request.json)

    # if validate(request.json, schema):
    #     print(True)
    # else:
    #     print(False)

    receipt = request.json

    id = str(uuid.uuid4())

    in_mem_db[id] = receipt

    return { "id": id }

def get_points(id):
    return { "points": in_mem_db[id] }

def __score_points(receipt):
    pass

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def validateReceipt(receipt):
    return rschema.validateReceipt(receipt)