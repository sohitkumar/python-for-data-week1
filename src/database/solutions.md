# Stage 1 :

select * from employees;
select id, first_name, last_name, department, title from employees;
select distinct department from employees;
select id, first_name, last_name, salary from employees order by salary;
select * from employees offset 20 limit 10;
select * from employees offset 40 limit 5;