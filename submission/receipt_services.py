import uuid
import json
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from openapi_schema_validator import validate
import math
from datetime import datetime

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
    total += __score_item_descriptions(receipt)
    total += __score_date(receipt)
    total += __score_time(receipt)

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

def __score_item_descriptions(receipt):
    score = 0.0
    for item in receipt['items']:
        if len(item['shortDescription']) % 3 == 0:
            item_score = float(item['price']) * 0.2
            score += math.ceil(item_score)

    return int(score)


def __score_date(receipt):
    score = 0

    day = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d').date()
    
    if __is_odd(day.day):
        score += 6

    return score

def __score_time(receipt):
    score = 0

    time = datetime.strptime(receipt['purchaseTime'], '%H:%M')

    if __is_in_time_range(time):
        score += 10

    return score

def __is_odd(num):
    if num % 2 != 0:
        return True
    return False

def __is_in_time_range(time):

    if 14 < time.hour < 16:
        return True
    
    return False


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

def validateReceipt(receipt):
    return rschema.validateReceipt(receipt)