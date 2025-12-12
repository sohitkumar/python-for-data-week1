# Mini Projects — Problems

Use files from data/input and write outputs to data/output.

## 1) Clean and Export CSV Summary
- Input: data/input/messy_data.csv
- Expected Output: data/output/clean.csv and data/output/summary.json of changes
- Run: python src/mini_projects/clean_and_export_csv.py data/input/messy_data.csv data/output/clean.csv data/output/summary.json

## 2) Summary Report
- Input: data/input/employees.csv
- Expected Output: printed summary (counts, averages by department)
- Run: python src/mini_projects/summary_report.py data/input/employees.csv

## 3) Log Error Counter
- Input: data/input/logs.txt
- Expected Output: totals of ERROR/WARNING/INFO
- Run: python src/mini_projects/log_error_counter.py data/input/logs.txt

## 4) CSV Inner Join
- Input: students_part1.csv & students_part2.csv on student_id
- Expected Output: inner join CSV at data/output/joined.csv
- Run: python src/mini_projects/csv_inner_join.py data/input/students_part1.csv data/input/students_part2.csv data/output/joined.csv

## 5) Find Duplicates in CSV
- Input: any CSV (e.g., employees.csv)
- Expected Output: duplicated rows in data/output/duplicates.csv
- Run: python src/mini_projects/find_duplicates_in_csv.py data/input/employees.csv data/output/duplicates.csv
