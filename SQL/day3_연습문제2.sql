-- 함수 연습문제 3
-- 1
SELECT sysdate
FROM dual;

--2
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary"
FROM employees;

--3
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary",
       salary*0.155 "Increase"
FROM employees;

--5.1
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, 'J') = 1 or instr(last_name, 'A') = 1 
    or instr(last_name, 'M') = 1 ;

--5.2 
ACCEPT star_name PROMPT '시작문자 입력 : '
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, '&star_name') = 1;

--치완변수사용하면 이렇게 신기방기
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE last_name LIKE '&star_name%';  --요게 입력을 받는 값인 것.

--7
SELECT last_name||' earns $'||to_char(salary, '99,999')
        ||' monthly but wants $'
        ||to_char(salary*3, '99,999')||'.' as "Dream Salaries"
FROM employees;

--6
SELECT last_name, trunc(months_between(sysdate, hire_date)) "MONTHS_WORKED"
FROM employees;

--8
SELECT last_name, lpad(salary, 10, '$')
FROM employees;

--9 
SELECT last_name, hire_date,
    to_char(next_day(add_months(hire_date, 6), 2),
    'fmDay, "the" DDspth "of"  Month, YYYY') "REVIEW"
FROM employees;

--10 
SELECT last_name, hire_date, 
    to_char(hire_date, 'dy') "day"
FROM employees;

--11  
SELECT last_name, 
    decode(commission_pct, null,'No Commission', commission_pct) "COMM"
FROM employees;

--12 '*'을 어떻게 반복해서 출력할 수 있는지 모르겠습니다..
SELECT last_name||' '||(salary/1000)
    as "EMPLOYEES_AND_THEIR_SALARIES"
FROM employees;

--13
SELECT job_id,decode(job_id, 'AD_PRES', 'A',
                    'ST_MAN', 'B',
                    'IT_PROG', 'C',
                    'SA_REP', 'D',
                    'ST_CLERK', 'E', '0') "GRA"
FROM employees;



--그룹함수 연습문제---------------------------------------------
--1
Group functions work across many rows to produce one result per group.
 > True

--2	
Group functions include nulls in calculations.
 > False

--3
The WHERE clause restricts rows before inclusion in a group calculation.
 > True

--4 
SELECT max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", avg(salary) "Average"
FROM employees;

--5 
SELECT job_id, max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", trunc(avg(salary)) "Average"
FROM employees
GROUP BY job_id
ORDER BY 1;

--6
SELECT job_id, count(*)
FROM employees
GROUP BY job_id
ORDER BY 1;

--7 null 포함 count는 어떻게 하는지 모르겠습니다.. 
SELECT count(e.employee_id) "Numer of Managers"
FROM employees e join departments d
    on d.manager_id = e.employee_id;

-- 8
SELECT (max(salary) - min(salary)) "DIFFERENCE"
FROM employees;

--9 
SELECT manager_id, min(salary)
FROM employees 
GROUP BY manager_id
HAVING manager_id is not null and min(salary) > 6000
ORDER BY 2 desc;

--10
SELECT count(*) "TOTAL"
    , sum(decode(to_char(hire_date, 'YYYY'),1995, 1, 0)) "1995"
    , sum(decode(to_char(hire_date, 'YYYY'),1996, 1, 0)) "1996"
    , sum(decode(to_char(hire_date, 'YYYY'),1997, 1, 0)) "1997"
    , sum(decode(to_char(hire_date, 'YYYY'),1998, 1, 0)) "1998"
FROM employees;

--11 
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


--조인 연습문제-----------------------------------
--1
SELECT location_id, street_address, city, 
    state_province, country_id
FROM locations;

--2
SELECT e.last_name, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id;

--3 
SELECT e.last_name, e.job_id, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id
    join locations l
    on d.location_id = l.location_id and
    l.city = 'Toronto';

--4
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a join employees b 
   on a.manager_id = b.employee_id
ORDER BY 4, 2;

--5
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 2;

--6
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 1;

--7 
SELECT e.last_name, e.job_id, 
    d.department_name, e.salary, j.grade_level "gra"
FROM employees e  join departments d 
   on d.manager_id = e.manager_id
   join job_grades j 
   on e.salary
   between j.lowest_sal and j.highest_sal
ORDER BY 5;

--8 
SELECT last_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date  
                    FROM employees
                    WHERE last_name = 'Davies');

--9 null이 빠지고 검색이 되는데 포함을 어떻게 하는지 모르겠습니다..
SELECT last_name, hire_date
FROM employees
WHERE hire_date
        not in (SELECT e.hire_date
            FROM employees e, departments d
            WHERE e.employee_id = d.manager_id);
