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

    receipt['points'] = __score_points(receipt=receipt)

    id = str(uuid.uuid4())

    in_mem_db["hi"] = receipt

    return { "id": id }

def get_points(id):
    return { "points": in_mem_db[id]['points'] }

def __score_points(receipt):
    total = 0
    total +=  __score_retailer_points(receipt)
    total +=  __score_dollar_amount(receipt)
    total += __score_item_counts(receipt)
    return total

def __score_retailer_points(receipt):
    return len(receipt["retailer"])

def __score_dollar_amount(receipt):
    score = 0
    if float(receipt['total']) % 1.00 == 0:
        score += 50
    if float(receipt['total']) % 0.25 == 0:
        score += 25
    return score
    
def __score_item_counts(receipt):
    score = 0
    score =+ len(receipt['items']) // 2 * 5
    return score
    
     

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def validateReceipt(receipt):
    return rschema.validateReceipt(receipt)