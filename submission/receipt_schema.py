import json
import jsonschema

# Describe what kind of json you expect.
receiptSchema = {
    "type": "object",
    "properties": {
        "retailer": {"type": "string"},
        "purchaseDate": {"type": "date"},
        "purchaseTime": {"type": "time"},
        "total": "2.65",
        "items": [
            {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
            {"shortDescription": "Dasani", "price": "1.40"}
        ]
    }
}

def validateReceipt(jsonData):
    try:
       jsonschema.validate(instance=jsonData, schema=receiptSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True