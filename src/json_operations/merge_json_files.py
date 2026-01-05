import json
from pathlib import Path

input_path = Path("data/input")
merged_list = []
for file in sorted(input_path.glob("*.json")):
    with open(file) as f:
        data = json.load(f)
        if isinstance(data, dict):
            data["source"] = f.name
            merged_list.append(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    item["source"] = f.name
                merged_list.append(data)

with open("data/output/merged.json", "w") as f:
    json.dump(merged_list, f, indent=2)