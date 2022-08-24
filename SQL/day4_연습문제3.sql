--1 Zlotkey����� ���� �μ��� �ٹ��ϴ� ��� ������ �˻� (Zlotkey����� ����)
SELECT last_name, hire_date
FROM employees
WHERE department_id = (SELECT department_id
                    FROM employees
                    WHERE last_name = 'Zlotkey')
    and last_name != 'Zlotkey';

--2 ��ü ����� ��տ��޺��� ������ ���� �޴� ��� �˻� (������ ������������ ����)
SELECT employee_id, last_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
                FROM employees)
ORDER BY 3;

--3 last_name�� 'u' ���ڰ� ���ԵǾ� �ִ� ������ ���� �μ����� ���ϴ� ��� �˻�
SELECT employee_id, last_name
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%');


--4 location ID �� 1700�� �μ��� �ٹ��ϴ� ��� �˻�
SELECT e.last_name, e.department_id, e.job_id
FROM employees e, departments d
WHERE e.department_id = d.department_id 
    and d.location_id = 1700;

--�������� ���
select last_name, department_id, job_id
from employees
where department_id in (select department_id
                        from departments
                        where location_id = 1700)
order by 2, 3;


--5 King������� ���� �����ϴ� ��� ��� �˻�(King����� �����ڷ� ������ ��� ��� �˻�)
SELECT last_name, salary
FROM employees 
WHERE manager_id = (SELECT employee_id
                    FROM employees
                    WHERE last_name = 'King');

--6 'Executive' �μ��� �ٹ��ϴ� ��� �˻�
SELECT department_id, last_name, job_id
FROM employees 
WHERE department_id = (SELECT department_id
                    FROM departments
                    WHERE department_name = 'Executive');

--7 lastname�� 'u'�� ���Ե� ������ ���� �μ��� �ٹ��ϸ鼭 ��ü ����� 
--  ��տ��޺��� ������ ���� �޴� ��� �˻�
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%')
    AND salary > (SELECT avg(salary)
                FROM employees);
