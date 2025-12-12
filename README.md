# Python for Data – Week 1

Practice exercises for Python fundamentals used in data engineering and analysis. Bring your own CSV/JSON files to the data/input folder and run the scripts to practice.

## Topics Covered
- Lists, Dicts, Tuples
- CSV & JSON File Handling
- Exceptions & Functions
- Data Cleaning Tasks

## Quick Start

1) Create and activate a virtualenv, then install deps:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2) Create input/output folders (if not present):

```bash
mkdir -p data/input data/output
```

3) Drop your practice files (CSV/JSON/TXT) into data/input and run any script under src/**.

Example:

```bash
python src/csv_operations/read_csv_count_rows.py data/input/employees.csv
python src/csv_operations/filter_csv_by_salary.py data/input/employees.csv 70000
python src/json_operations/convert_csv_to_json.py data/input/employees.csv data/output/employees.json
```

## Suggested Data Inputs (Bring Your Own)

Place these files in data/input/ with the suggested schemas. You can change column names—just adapt script arguments if needed.

- employees.csv
  - Columns: id,name,department,salary,join_date
  - Notes: Include varied salaries and some missing values to test cleaning.

- students_part1.csv, students_part2.csv
  - Columns: student_id,name,batch,score
  - Notes: Use overlapping student_ids for join/merge exercises.

- messy_data.csv
  - Columns: mix of numeric/text with blanks, extra spaces, inconsistent casing.
  - Notes: Ideal for cleaning: trim spaces, normalize case, fill/drop nulls.

- categories.csv
  - Columns: id,category,parent_id
  - Notes: Try hierarchical relationships for flattening and lookups.

- logs.txt
  - Free-form lines containing timestamps, levels, and messages.
  - Notes: Useful for counting errors/warnings and parsing patterns.

- sample.json
  - JSON array of objects, e.g. [{"id":1,"name":"Alice","tags":["a","b"]}].
  - Notes: Include nested fields to practice flattening and field extraction.

## Practice Questions (Inputs Only)

Use the scripts in src/** to solve these. Each bullet is a problem prompt; supply your own input files.

### Lists, Dicts, Tuples
- Remove duplicates from a list of integers and preserve order.
- Count occurrences of words in a list and return a dict sorted by frequency.
- Sort a list of dicts by age ascending and then by name.
- Extract even numbers from a mixed list and return a new list.
- Convert a list of (key, value) tuples into a dict.

### CSV Operations
- Count the number of rows in employees.csv and print the total.
- Filter rows where salary >= X and write to data/output/filtered.csv.
- Combine students_part1.csv and students_part2.csv into data/output/combined.csv with de-duplicated student_ids.
- Count missing values per column in messy_data.csv and print a summary.
- Clean messy_data.csv (trim spaces, standardize casing, handle nulls) and write data/output/clean.csv.

### JSON Operations
- Convert employees.csv to JSON and save to data/output/employees.json.
- Merge multiple JSON files in data/input into one data/output/merged.json.
- Flatten nested JSON objects from sample.json and write a flat version.
- Extract only selected fields (e.g., id, name) from sample.json.
- Convert a JSON array to CSV and save to data/output/converted.csv.

### Functions & Exceptions
- Implement safe_divide(a, b) that handles division by zero gracefully.
- Write a safe file reader that returns a default value when the file is missing.
- Validate email strings and return whether they match a basic pattern.
- Define and raise a custom exception for invalid input data.
- Compute the average of a list while skipping non-numeric values.

### Mini Projects
- Clean messy_data.csv and export a summary JSON of changes.
- Generate a consolidated summary report (counts, averages) from employees.csv.
- Count occurrences of ERROR and WARNING in logs.txt and output totals.
- Perform an inner join of students_part1.csv and students_part2.csv on student_id.
- Detect duplicate rows in an input CSV and output the duplicates file.

## Repository Layout

python-for-data-week1/
│
├── README.md
├── requirements.txt
├── data/
│   ├── input/              # Put your CSV/JSON/TXT inputs here
│   └── output/             # Scripts write results here
├── src/                    # Exercise scripts grouped by topic
└── tests/                  # Unit tests for reference

## Tips
- Keep raw inputs in data/input and never overwrite them; write outputs to data/output.
- Many scripts accept command-line args; run with -h for usage if available.
- Start small: create tiny CSVs (5–10 rows) to validate behavior before scaling.
