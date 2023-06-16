import uuid
import json
import receipt_schema as rschema

def process_receipt(request):

    return { "id": str(uuid.uuid4()) }

def get_points(id):
    return "<p>Hello, points {}!</p>".format(id)

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