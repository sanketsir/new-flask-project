import json
def load_json():
    with open("products1.json") as f:
        return json.load(f)
db=load_json()