import json

def get_shipment(shipment_id):

    with open("data/shipments.json","r") as file:
        shipments = json.load(file)

    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment

    return None