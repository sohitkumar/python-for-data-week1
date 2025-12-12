# Functions & Exceptions — Problems

## 1) safe_divide(a, b)
- Input: a=10, b=0
- Expected Output: "Division by zero" or a safe default (e.g., None)

## 2) safe_file_reader(path, default)
- Input: path=nonexistent.txt, default="N/A"
- Expected Output: "N/A"

## 3) validate_email(s)
- Input: "alice@example.com"
- Expected Output: True
- Input: "invalid@"
- Expected Output: False

## 4) custom_exceptions
- Task: Raise `InvalidDataError` when input list is empty.
- Input: []
- Expected Output: Exception raised.

## 5) average_of_list(values)
- Input: [1, 2, "x", 3]
- Expected Output: 2.0 (skips non-numeric)
