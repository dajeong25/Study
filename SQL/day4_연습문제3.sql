--1
SELECT last_name, hire_date
FROM employees
WHERE department_id = (SELECT department_id
                    FROM employees
                    WHERE last_name = 'Zlotkey')
    and last_name != 'Zlotkey';

--2
SELECT employee_id, last_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
                FROM employees)
ORDER BY 3;

--3
SELECT employee_id, last_name
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%');

--4
SELECT e.last_name, e.department_id, e.job_id
FROM employees e, departments d
WHERE e.department_id = d.department_id 
    and d.location_id = 1700;

--5
SELECT last_name, salary
FROM employees 
WHERE manager_id = (SELECT employee_id
                    FROM employees
                    WHERE last_name = 'King');

--6
SELECT department_id, last_name, job_id
FROM employees 
WHERE department_id = (SELECT department_id
                    FROM departments
                    WHERE department_name = 'Executive');

--7
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%')
    AND salary > (SELECT avg(salary)
                FROM employees);
