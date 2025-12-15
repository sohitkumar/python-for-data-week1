# Employees SQL Practice — Questions Only (PostgreSQL)

Use these prompts to write queries yourself. They map 1:1 with the practice stages in `employees_sql_practice.md`. Assume a table `employees` with columns:
- id, first_name, last_name, email, department, title, salary, hire_date, manager_id, status

---

## Stage 1 — Select Basics
1. Return all columns and rows from `employees`.
2. Return only `id`, `first_name`, `last_name`, `department`, `title`.
3. List unique departments.
4. List `id`, `first_name`, `last_name`, `salary` sorted by salary descending and last name ascending.
5. Paginate employees: page size 10, fetch page 3.

## Stage 2 — Filtering (WHERE)
6. Find employees earning more than 80,000.
7. Show active employees in Engineering.
8. Find all emails from the `example.com` domain.
9. Show employees in any of: Engineering, Product, Design.
10. Show employees with no manager assigned.

## Stage 3 — Aggregations
11. Count total employees.
12. Compute average salary overall.
13. For each department, count employees, sorted by largest headcount.
14. For each department, compute average salary for active vs inactive employees.
15. Show departments whose average salary exceeds 90,000.

## Stage 4 — Derived Columns & Conditionals
16. Show `salary` alongside a computed 10% raise.
17. Classify employees into `high` (≥150k), `medium` (≥90k), `low` based on salary.

## Stage 5 — Date & Time
18. List employees hired on or after 2024‑01‑01.
19. Show years of service for each employee (today vs `hire_date`).
20. Group hires by month (YYYY‑MM), count hires per month.

## Stage 6 — Self‑Joins (Managers)
21. Show each employee with their manager (id + first name).
22. For each manager, count direct reports; sort by largest team.

## Stage 7 — Subqueries
23. Show top earners (≥ 90th percentile of salary).
24. Show each employee with the overall average salary as a separate column.
25. List managers who have at least 5 direct reports (use `EXISTS`).

## Stage 8 — CTEs (WITH)
26. Build a department stats CTE (`avg_salary`, `headcount`) and select from it.
27. Use two CTEs: `active` and `inactive`; return both counts in one row.

## Stage 9 — Window Functions
28. Rank salaries within each department (highest first).
29. Compute running total of salaries ordered by `id` within each department.
30. Compute percent rank of salary within each department.

## Stage 10 — Set Operations
31. Union unique titles from active and inactive employees.
32. Intersect departments that have managers with departments that are active.

## Stage 11 — DML (Insert/Update/Delete)
33. Insert a new employee row with realistic values.
34. Give Engineering employees earning <110k a 5% raise and prefix title with "Senior".
35. Soft‑delete (set `status = 'terminated'`) a specific employee by `id`.
36. Delete terminated employees hired more than 2 years ago.

## Stage 12 — Constraints & Validation
37. Find emails that do not match a standard email pattern.
38. Find employees with negative salaries.

## Stage 13 — Indexing (Conceptual)
39. Identify which columns should be indexed based on common filters and joins.
40. Write index creation statements for those columns.

## Stage 14 — JSON & Text Helpers (Optional)
41. Extract the domain (part after `@`) from each email.
42. Run a basic full‑text search to find titles containing "engineer".

## Stage 15 — Practical Reports
43. For each department, show headcount, average salary (rounded), earliest and latest hire date; sort by headcount.
44. For each manager, show full name, team size, and average team salary; sort by team size.

---

Tips:
- Write first, then verify by comparing with `employees_sql_practice.md`.
- Try variations: add filters, change sort orders, use `DISTINCT` where relevant.
- Prefer explicit column lists over `SELECT *` in production queries.
