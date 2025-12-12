# JSON Operations — Problems

Use files from data/input.

## 1) CSV to JSON
- Input: data/input/employees.csv
- Expected Output: data/output/employees.json
- Run: python src/json_operations/convert_csv_to_json.py data/input/employees.csv data/output/employees.json

## 2) Merge JSON Files
- Input: all JSON files in data/input
- Expected Output: data/output/merged.json (array or merged object)
- Run: python src/json_operations/merge_json_files.py data/input data/output/merged.json

## 3) Flatten JSON
- Input: data/input/sample.json (nested)
- Expected Output: flattened JSON objects
- Run: python src/json_operations/flatten_json.py data/input/sample.json data/output/flat.json

## 4) Extract Fields
- Input: data/input/sample.json
- Expected Output: only selected fields (e.g., id, name)
- Run: python src/json_operations/extract_fields.py data/input/sample.json data/output/extracted.json id name

## 5) JSON to CSV
- Input: data/input/sample.json
- Expected Output: data/output/converted.csv
- Run: python src/json_operations/convert_json_to_csv.py data/input/sample.json data/output/converted.csv
