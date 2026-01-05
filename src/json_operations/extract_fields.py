import json

with open("data/input/sample.json", "r") as f:
    data = json.load(f)
l = []
for item in data:
    d = {
        "id" : item.get("id"),
        "name" : item.get("name")
    }
    l.append(d)
with open("data/output/extracted.json", "w") as f:
    json.dump(l, f)