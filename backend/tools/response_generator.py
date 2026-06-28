def generate_response(shipment):

    return f"""
Shipment ID: {shipment['id']}

Status: {shipment['status']}

Current Location: {shipment['location']}

Expected Delivery: {shipment['delivery']}

Thank you for contacting CargoMind AI Support.
"""