import re

def extract_shipment_id(message):

    pattern = r"DEX\d+"

    match = re.search(pattern, message)

    if match:
        return match.group()

    return None