
def palce_order_for_pet(shipDate, quantity):
    body = {
        "id": 0,
        "petId": 0,
        "quantity": quantity,
        "shipDate": shipDate,
        "status": "placed",
        "complete": "true"
    }
    return body
