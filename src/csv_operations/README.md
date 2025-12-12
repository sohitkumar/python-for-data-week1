# CSV Operations — Problems

Use files from data/input.

## 1) Count Rows
- Input: data/input/employees.csv
- Expected Output: Total rows (e.g., 25)
- Run: python src/csv_operations/read_csv_count_rows.py data/input/employees.csv

## 2) Filter by Salary
- Input: data/input/employees.csv, threshold=80000
- Expected Output: data/output/filtered.csv with rows salary >= 80000
- Run: python src/csv_operations/filter_csv_by_salary.py data/input/employees.csv 80000

## 3) Combine Two CSVs
- Input: students_part1.csv + students_part2.csv
- Expected Output: data/output/combined.csv (deduped by student_id)
- Run: python src/csv_operations/combine_two_csv.py data/input/students_part1.csv data/input/students_part2.csv data/output/combined.csv

## 4) Count Missing Values
- Input: data/input/messy_data.csv
- Expected Output: printed per-column missing counts
- Run: python src/csv_operations/count_missing_values.py data/input/messy_data.csv

## 5) Clean CSV Data
- Input: data/input/messy_data.csv
- Expected Output: data/output/clean.csv (trim spaces, normalize case, handle blanks)
- Run: python src/csv_operations/clean_csv_data.py data/input/messy_data.csv data/output/clean.csv
