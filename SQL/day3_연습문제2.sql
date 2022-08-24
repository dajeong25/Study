--�Լ� ��������-------------------------------------------------
-- 1 ���� ��¥�� ����ϴ� query���� �ۼ��Ͻÿ� 
SELECT sysdate
FROM dual;

--2 Employees ���̺��� ����� ��ȣ, �̸�, �޿��� 15.5% �λ�� �޿��� 
--  ����ϴ� query���� �ۼ��Ͻÿ�.
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary"
FROM employees;

--3. 2���� ��°���� ���� �޿��� �λ�� �޿��� ������ ���̸� ����ϴ� 
--   query���� �ۼ��Ͻÿ�
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary",
       salary*0.155 "Increase"
FROM employees;

--5.1 Employees ���̺��� ��� data��  last name �÷����� ���۹��ڰ�
-- J �Ǵ� A, M�� �����ϴ� ����̸��� lastName �̸� ���̸� ����ϴ� query���� �ۼ��Ͻÿ� 
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, 'J') = 1 or instr(last_name, 'A') = 1 
    or instr(last_name, 'M') = 1 ;

--5.2 query �� ���ۼ��Ͽ� ���۹��ڸ� �Է¹ް�, �Է¹��� ���ڷ� �����ϴ� 
--    lastname�� lastname�� ���̸� query���� �ۼ��Ͻÿ�
ACCEPT star_name PROMPT '���۹��� �Է� : '
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, '&star_name') = 1;
--#2 ġ�Ϻ��� ���
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE last_name LIKE '&star_name%';  --��� �Է��� �޴� ���� ��.


--7 ������ �������� ����ϴ� query�� �ۼ��Ͻÿ�
-- <employee last name> earns <salary> monthly but wants <3 times salary>. 
-- �÷� Ÿ��Ʋ�� Dream Salaries.
SELECT last_name||' earns $'||to_char(salary, '99,999')
        ||' monthly but wants $'
        ||to_char(salary*3, '99,999')||'.' as "Dream Salaries"
FROM employees;

--6 Employees ���̺��� ��� data��  last name�� �Ի��� ����, �ٹ��� 
--  �������� �Ʒ� ���� �������� ����ϴ� query�� �ۼ��Ͻÿ� 
SELECT last_name, trunc(months_between(sysdate, hire_date)) "MONTHS_WORKED"
FROM employees;

--8 employees  ���̺��� ��� �����  last name �� salary�� ������ ��������
--  ����ϴ� query�� �ۼ��Ͻÿ�
SELECT last_name, lpad(salary, 10, '$')
FROM employees;

--9 employee��s last name, hire date, �޿� ���ͺ� ��¥�� ������ �������� ����Ͻÿ�
-- �Ի��� 6���� �� ������ ��Monday, the Thirty-First of July, 2000.��
SELECT last_name, hire_date,
    to_char(next_day(add_months(hire_date, 6), 2),
    'fmDay, "the" DDspth "of"  Month, YYYY') "REVIEW"
FROM employees;

--10 �� ������� �Ի糯¥�� ������ ����Ͻÿ�
SELECT last_name, hire_date, 
    to_char(hire_date, 'dy') "day"
FROM employees;

--11 the employees�� last names ��  commission �� ����Ͻÿ�
--   Ŀ�̼��� ���� ���� ����� ��No Commission.�� ���� ����Ͻÿ�

SELECT last_name, 
    decode(commission_pct, null,'No Commission', commission_pct) "COMM"
FROM employees;

--12 employees�� last name�� �޿��� 1000�޷� ������  
--   asterisks�� �Բ� ���� �÷�������  ����Ͻÿ�
--   �÷�heading�� EMPLOYEES_AND_THEIR_SALARIES.
SELECT rpad(last_name||' ',length(last_name)+trunc(salary/1000), '*')
    as "EMPLOYEES_AND_THEIR_SALARIES"
FROM employees
ORDER BY salary desc;

--13 DECODE �Լ��� case ǥ������ ����ؼ�  ���� ǥó�� �������� grade�� ����Ͻÿ�
SELECT job_id,decode(job_id, 'AD_PRES', 'A',
                    'ST_MAN', 'B',
                    'IT_PROG', 'C',
                    'SA_REP', 'D',
                    'ST_CLERK', 'E', '0') "GRA"
FROM employees;


--�׷��Լ� ��������---------------------------------------------
--1
Group functions work across many rows to produce one result per group.
 > True

--2	
Group functions include nulls in calculations.
 > False

--3
The WHERE clause restricts rows before inclusion in a group calculation.
 > True

--4 ��ü ��� data�߿��� . ������ �ִ밪, �ּҰ�, �հ�, ����� ����Ͻÿ�
--  �÷� Ÿ��Ʋ Maximum, Minimum, Sum, Average
SELECT max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", avg(salary) "Average"
FROM employees;

--5 ������ ������ �ִ밪, �ּҰ�, �հ�, ����� ����Ͻÿ� 
--  �÷� Ÿ��Ʋ Maximum, Minimum, Sum, Average
SELECT job_id, max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", trunc(avg(salary)) "Average"
FROM employees
GROUP BY job_id
ORDER BY 1;

--6 ������ ������� ����Ͻÿ�
SELECT job_id, count(*)
FROM employees
GROUP BY job_id
ORDER BY 1;

--7 �������� ����� ���� ����Ͻÿ�
SELECT count(distinct manager_id) "Numer of Managers"
FROM employees; 

-- 8 Employees ����� �ּ� ���ް� �ִ������ ���̸� ����Ͻÿ�
SELECT (max(salary) - min(salary)) "DIFFERENCE"
FROM employees;

--9 Employees ���̺� �����ڰ� ���� ����� �����ϰ� �����ڷ� �׷��ε� 
--  �����(�ǰ�����) �߿��� ���� ���� ������ �޴� ������� �ּұ޿��� 
--  6000�̻��� ���ڵ带 �ּұ޿��� ������������ ����Ͻÿ�
SELECT manager_id, min(salary)
FROM employees 
GROUP BY manager_id
HAVING manager_id is not null and min(salary) > 6000
ORDER BY 2 desc;

--10 ��ü �����, 1995, 1996, 1997, 1998�⵵�� �Ի��� ������� ����Ͻÿ�
--   �÷� Ÿ��Ʋ�� total,  1995, 1996, 1997, 1998 �� ����Ͻÿ�
SELECT count(*) "TOTAL" --���ϴ� ��. �׷��� decode�� case when ���
    , sum(decode(to_char(hire_date, 'YYYY'),1995, 1, 0)) "1995"
    , sum(decode(to_char(hire_date, 'YYYY'),1996, 1, 0)) "1996"
    , sum(decode(to_char(hire_date, 'YYYY'),1997, 1, 0)) "1997"
    , sum(decode(to_char(hire_date, 'YYYY'),1998, 1, 0)) "1998"
FROM employees;

--11 �������� ������ �հ��   �� �μ����� ������ ������ �հ踦 �Ʒ� ����� ���� ����Ͻÿ�  
--   �÷� Ÿ��Ʋ�� Job, Dept 20, Dept 50, Dept 80, Dept 90�� ����Ͻÿ�
SELECT job_id,  sum(salary) "Dept 20", to_number(null) "Dept 50",
    to_number(null) "Dept 80", to_number(null) "Dept 90",
    sum(salary) "Total"
FROM employees
GROUP BY job_id, department_id
HAVING department_id = 20
union all
SELECT job_id, to_number(null) "Dept 20",
     sum(salary) "Dept 50", to_number(null) "Dept 80",
    to_number(null) "Dept 90",sum(salary) "Total"
FROM employees
GROUP BY job_id, department_id
HAVING department_id = 50
union all
SELECT job_id, to_number(null) "Dept 20", to_number(null) "Dept 50",
     sum(salary) "Dept 80", to_number(null) "Dept 90",
    sum(salary) "Total"
FROM employees
GROUP BY job_id, department_id
HAVING department_id = 80
union all
SELECT job_id, to_number(null) "Dept 20", to_number(null) "Dept 50",
    to_number(null) "Dept 80",  sum(salary) "Dept 90", 
    sum(salary) "Total"
FROM employees
GROUP BY job_id, department_id
HAVING department_id = 90
ORDER BY 1;

--decode ���
SELECT job_id,
       decode(department_id,20,sum_sal) "Dept 20",
       decode(department_id,50,sum_sal) "Dept 50",
       decode(department_id,80,sum_sal) "Dept 80",
       decode(department_id,90,sum_sal) "Dept 90", sum_sal "Total"
       FROM (SELECT job_id, department_id, sum(salary) sum_sal
             FROM employees 
             group by department_id, job_id);


--���� ��������-----------------------------------
--1 ��� ����� �Ҽ� �μ��� �ּҸ� ����Ͻÿ�
SELECT location_id, street_address, city, 
    state_province, country_id
FROM locations;

--2 ������� last_name�� �μ���ȣ�� �μ��̸��� ����Ͻÿ�
SELECT e.last_name, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id;

--3 Toronto���� �ٹ��ϴ� �������(last_name, ����, �μ���ȣ, �μ��̸�)�� ����Ͻÿ� 
SELECT e.last_name, e.job_id, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id
    join locations l
    on d.location_id = l.location_id and
    l.city = 'Toronto';

--4 �����ȣ(last_name), ����̸�, �����ڹ�ȣ, ������ �̸�(last_name)�� ����Ͻÿ�
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a join employees b 
   on a.manager_id = b.employee_id
ORDER BY 4, 2;

--5 4������ �����ڰ� ���� King��� �����Ͱ� �����Ǿ����ϴ�.
--  �����ڰ� ���� King��� �����͸� �����Ͽ� �����ȣ(last_name), 
--  ����̸�, �����ڹ�ȣ, ������ �̸�(last_name)�� ����Ͻÿ�
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 2;

--6 ��� ����� ���ؼ� ������ �μ��� �ٹ��ϴ� �������̸�(last_name)�� 
--  �Բ� ����Ͻÿ�
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 1;

--7 ����̸�, ����, �μ��̸�, �޿�, ����� ����Ͻÿ�
SELECT e.last_name, e.job_id, 
    d.department_name, e.salary, j.grade_level "gra"
FROM employees e  join departments d 
   on d.manager_id = e.manager_id
   join job_grades j 
   on e.salary
   between j.lowest_sal and j.highest_sal
ORDER BY 5;

--8 Davies. ��� �Ի糯¥ ���Ŀ� �Ի��� ��� ����� �̸��� �Ի糯¥�� ����Ͻÿ�
SELECT last_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date  
                    FROM employees
                    WHERE last_name = 'Davies');

--9 ������߿��� ������� �����ں��� ���� �Ի��� ������� �Ʒ��� ���� ����Ͻÿ�
SELECT e.last_name last_name, e.hire_date hire_date,
     m.last_name last_name, m.hire_date hire_date
FROM employees e, employees m
WHERE e.manager_id = m.employee_id
    and e.hire_date < m.hire_date;
