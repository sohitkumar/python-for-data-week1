# Employees SQL Practice – Staged Query Drills (PostgreSQL)

This guide provides progressive practice queries focused on an `employees` table. Use it end-to-end or jump to stages you want to drill. Queries are written in PostgreSQL dialect but are broadly compatible.

Assumed schema (adapt as needed):
- id (INT, PK)
- first_name (TEXT)
- last_name (TEXT)
- email (TEXT)
- department (TEXT)
- title (TEXT)
- salary (NUMERIC)
- hire_date (DATE)
- manager_id (INT, FK to employees.id or NULL)
- status (TEXT) — e.g., 'active', 'on_leave', 'terminated'

If your actual columns differ, adjust column names in the queries accordingly.

---

## Stage 1 — Select Basics
- List all employees
```sql
SELECT * FROM employees;
```
- Select specific columns
```sql
SELECT id, first_name, last_name, department, title FROM employees;
```
- Remove duplicates
```sql
SELECT DISTINCT department FROM employees;
```
- Simple ordering
```sql
SELECT id, first_name, last_name, salary
FROM employees
ORDER BY salary DESC, last_name ASC;
```
- Limit and offset (pagination)
```sql
SELECT id, first_name, last_name
FROM employees
ORDER BY id
LIMIT 10 OFFSET 20; -- page 3 if page size = 10
```

## Stage 2 — Filtering (WHERE)
- Basic comparisons
```sql
SELECT id, first_name, last_name, salary
FROM employees
WHERE salary > 80000;
```
- Multiple conditions
```sql
SELECT id, first_name, last_name, department
FROM employees
WHERE department = 'Engineering' AND status = 'active';
```
- Pattern matching
```sql
SELECT id, email
FROM employees
WHERE email ILIKE '%@example.com';
```
- IN / NOT IN
```sql
SELECT id, first_name, department
FROM employees
WHERE department IN ('Engineering', 'Product', 'Design');
```
- NULL checks
```sql
SELECT id, first_name, manager_id
FROM employees
WHERE manager_id IS NULL; -- no manager assigned
```

## Stage 3 — Aggregations
- Count employees
```sql
SELECT COUNT(*) AS total_employees FROM employees;
```
- Average salary
```sql
SELECT AVG(salary) AS avg_salary FROM employees;
```
- Group by department
```sql
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
ORDER BY headcount DESC;
```
- Aggregate with filter
```sql
SELECT
  department,
  AVG(salary) FILTER (WHERE status = 'active') AS avg_active_salary,
  AVG(salary) FILTER (WHERE status <> 'active') AS avg_inactive_salary
FROM employees
GROUP BY department;
```
- HAVING (post-aggregation filter)
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 90000
ORDER BY avg_salary DESC;
```

## Stage 4 — Derived Columns & Conditionals
- Computed columns
```sql
SELECT id, first_name, last_name, salary, salary * 1.10 AS salary_after_raise
FROM employees;
```
- CASE expressions
```sql
SELECT id, first_name, department,
  CASE
    WHEN salary >= 150000 THEN 'high'
    WHEN salary >= 90000 THEN 'medium'
    ELSE 'low'
  END AS salary_band
FROM employees;
```

## Stage 5 — Date & Time
- Employees hired after a date
```sql
SELECT id, first_name, hire_date
FROM employees
WHERE hire_date >= DATE '2024-01-01'
ORDER BY hire_date;
```
- Years of service
```sql
SELECT id, first_name, last_name,
  EXTRACT(YEAR FROM AGE(CURRENT_DATE, hire_date)) AS years_of_service
FROM employees
ORDER BY years_of_service DESC;
```
- Monthly cohort
```sql
SELECT TO_CHAR(hire_date, 'YYYY-MM') AS cohort_month, COUNT(*) AS hires
FROM employees
GROUP BY cohort_month
ORDER BY cohort_month;
```

## Stage 6 — Self-Joins (Managers)
- Employee to manager mapping
```sql
SELECT e.id AS employee_id, e.first_name AS employee_name,
       m.id AS manager_id, m.first_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id
ORDER BY employee_id;
```
- Team counts per manager
```sql
SELECT m.id AS manager_id, m.first_name AS manager_name, COUNT(e.id) AS team_size
FROM employees m
LEFT JOIN employees e ON e.manager_id = m.id
GROUP BY m.id, m.first_name
ORDER BY team_size DESC;
```

## Stage 7 — Subqueries
- Top earners (subquery in WHERE)
```sql
SELECT id, first_name, last_name, salary
FROM employees
WHERE salary >= (
  SELECT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY salary)
  FROM employees
)
ORDER BY salary DESC;
```
- Scalar subquery in SELECT
```sql
SELECT id, first_name, salary,
  (SELECT AVG(salary) FROM employees) AS avg_salary_all
FROM employees;
```
- EXISTS for managers with large teams
```sql
SELECT id, first_name, last_name
FROM employees e
WHERE EXISTS (
  SELECT 1
  FROM employees team
  WHERE team.manager_id = e.id
  GROUP BY team.manager_id
  HAVING COUNT(*) >= 5
);
```

## Stage 8 — CTEs (WITH)
- Department salary stats
```sql
WITH dept_stats AS (
  SELECT department, AVG(salary) AS avg_salary, COUNT(*) AS headcount
  FROM employees
  GROUP BY department
)
SELECT *
FROM dept_stats
ORDER BY avg_salary DESC;
```
- Active vs inactive split
```sql
WITH active AS (
  SELECT * FROM employees WHERE status = 'active'
), inactive AS (
  SELECT * FROM employees WHERE status <> 'active'
)
SELECT (SELECT COUNT(*) FROM active) AS active_count,
       (SELECT COUNT(*) FROM inactive) AS inactive_count;
```

## Stage 9 — Window Functions
- Rank salaries within department
```sql
SELECT id, first_name, department, salary,
  RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_salary_rank
FROM employees
ORDER BY department, dept_salary_rank;
```
- Running totals by department
```sql
SELECT department, id, salary,
  SUM(salary) OVER (PARTITION BY department ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_salary
FROM employees
ORDER BY department, id;
```
- Percentiles per department
```sql
SELECT id, department, salary,
  PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) AS dept_percent_rank
FROM employees;
```

## Stage 10 — Set Operations
- Union roles across statuses
```sql
SELECT DISTINCT title FROM employees WHERE status = 'active'
UNION
SELECT DISTINCT title FROM employees WHERE status <> 'active'
ORDER BY title;
```
- Intersect departments with managers (self-condition)
```sql
SELECT DISTINCT e.department
FROM employees e
WHERE e.manager_id IS NOT NULL
INTERSECT
SELECT DISTINCT d.department
FROM employees d
WHERE d.status = 'active'
ORDER BY department;
```

## Stage 11 — DML (Insert/Update/Delete)
- Insert new employee
```sql
INSERT INTO employees (id, first_name, last_name, email, department, title, salary, hire_date, manager_id, status)
VALUES (1001, 'Ava', 'Li', 'ava.li@example.com', 'Engineering', 'Software Engineer', 120000, DATE '2025-12-15', 200, 'active');
```
- Update salary and title
```sql
UPDATE employees
SET salary = salary * 1.05, title = 'Senior ' || title
WHERE department = 'Engineering' AND salary < 110000;
```
- Soft delete / deactivate
```sql
UPDATE employees
SET status = 'terminated'
WHERE id = 1001;
```
- Delete (use cautiously)
```sql
DELETE FROM employees
WHERE status = 'terminated' AND hire_date < CURRENT_DATE - INTERVAL '2 years';
```

## Stage 12 — Constraints & Validation (Conceptual)
- Validate emails
```sql
SELECT id, email
FROM employees
WHERE email !~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$';
```
- Check negative salaries
```sql
SELECT * FROM employees WHERE salary < 0;
```

## Stage 13 — Indexing (Conceptual + Checks)
- Identify columns frequently filtered: `department`, `status`, `manager_id`, `salary`, `hire_date`.
- Example index creation
```sql
CREATE INDEX IF NOT EXISTS idx_employees_department ON employees (department);
CREATE INDEX IF NOT EXISTS idx_employees_status ON employees (status);
CREATE INDEX IF NOT EXISTS idx_employees_manager ON employees (manager_id);
CREATE INDEX IF NOT EXISTS idx_employees_hire_date ON employees (hire_date);
-- For range queries:
CREATE INDEX IF NOT EXISTS idx_employees_salary ON employees (salary);
```

## Stage 14 — JSON & Text Helpers (If columns exist)
- Extract domain from email
```sql
SELECT id, email, split_part(email, '@', 2) AS email_domain
FROM employees;
```
- Basic full-text search (if `title` meaningful)
```sql
SELECT id, title
FROM employees
WHERE to_tsvector('english', title) @@ plainto_tsquery('english', 'engineer');
```

## Stage 15 — Practical Reports
- Department summary
```sql
SELECT department,
       COUNT(*) AS headcount,
       ROUND(AVG(salary)) AS avg_salary,
       MIN(hire_date) AS earliest_hire,
       MAX(hire_date) AS latest_hire
FROM employees
GROUP BY department
ORDER BY headcount DESC;
```
- Manager dashboards
```sql
SELECT m.id AS manager_id, m.first_name || ' ' || m.last_name AS manager_name,
       COUNT(e.id) AS team_size,
       ROUND(AVG(e.salary)) AS avg_team_salary
FROM employees m
LEFT JOIN employees e ON e.manager_id = m.id
GROUP BY m.id, manager_name
ORDER BY team_size DESC;
```

---

## Quick Run Tips
- Using `psql`:
```bash
psql "$DATABASE_URL" -c "SELECT COUNT(*) FROM employees;"
```
- Or open an interactive session:
```bash
psql "$DATABASE_URL"
-- then paste queries from this file
```

If you want, I can add a companion `.sql` file with the same stages for easy copy/paste into `psql`, or tailor queries to your exact `employees` schema once you share column names.