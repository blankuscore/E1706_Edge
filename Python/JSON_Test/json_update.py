import json

with open("data.json", "r") as jsonfile:
    data = json.load(jsonfile)

data["general"]["surge"] = "69"

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile)