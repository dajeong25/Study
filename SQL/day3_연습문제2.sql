--함수 연습문제-------------------------------------------------
-- 1 현재 날짜를 출력하는 query문을 작성하시오 
SELECT sysdate
FROM dual;

--2 Employees 테이블의 사원의 번호, 이름, 급여와 15.5% 인상된 급여를 
--  출력하는 query문을 작성하시오.
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary"
FROM employees;

--3. 2번의 출력결과에 현재 급여와 인상된 급여의 증가된 차이를 출력하는 
--   query문을 작성하시오
SELECT employee_id, last_name, salary, (salary*1.155) "New Salary",
       salary*0.155 "Increase"
FROM employees;

--5.1 Employees 테이블의 사원 data중  last name 컬럼값의 시작문자가
-- J 또는 A, M로 시작하는 사원이름과 lastName 이름 길이를 출력하는 query문을 작성하시오 
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, 'J') = 1 or instr(last_name, 'A') = 1 
    or instr(last_name, 'M') = 1 ;

--5.2 query 를 재작성하여 시작문자를 입력받고, 입력받은 문자로 시작하는 
--    lastname과 lastname의 길이를 query문을 작성하시오
ACCEPT star_name PROMPT '시작문자 입력 : '
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE instr(last_name, '&star_name') = 1;
--#2 치완변수 사용
SELECT last_name "Name", length(last_name) "Length"
FROM employees
WHERE last_name LIKE '&star_name%';  --요게 입력을 받는 값인 것.


--7 다음의 형식으로 출력하는 query를 작성하시오
-- <employee last name> earns <salary> monthly but wants <3 times salary>. 
-- 컬럼 타이틀은 Dream Salaries.
SELECT last_name||' earns $'||to_char(salary, '99,999')
        ||' monthly but wants $'
        ||to_char(salary*3, '99,999')||'.' as "Dream Salaries"
FROM employees;

--6 Employees 테이블의 사원 data중  last name과 입사한 이후, 근무한 
--  개월수를 아래 보기 형식으로 출력하는 query를 작성하시오 
SELECT last_name, trunc(months_between(sysdate, hire_date)) "MONTHS_WORKED"
FROM employees;

--8 employees  테이블의 모든 사원의  last name 과 salary를 다음의 형식으로
--  출력하는 query를 작성하시오
SELECT last_name, lpad(salary, 10, '$')
FROM employees;

--9 employee’s last name, hire date, 급여 인터뷰 날짜를 다음의 형식으로 출력하시오
-- 입사후 6개월 후 월요일 “Monday, the Thirty-First of July, 2000.”
SELECT last_name, hire_date,
    to_char(next_day(add_months(hire_date, 6), 2),
    'fmDay, "the" DDspth "of"  Month, YYYY') "REVIEW"
FROM employees;

--10 각 사원별로 입사날짜의 요일을 출력하시오
SELECT last_name, hire_date, 
    to_char(hire_date, 'dy') "day"
FROM employees;

--11 the employees’ last names 과  commission 을 출력하시오
--   커미션을 받지 않은 사원은 “No Commission.” 으로 출력하시오

SELECT last_name, 
    decode(commission_pct, null,'No Commission', commission_pct) "COMM"
FROM employees;

--12 employees’ last name과 급여를 1000달러 단위로  
--   asterisks를 함께 단일 컬럼값으로  출력하시오
--   컬럼heading은 EMPLOYEES_AND_THEIR_SALARIES.
SELECT rpad(last_name||' ',length(last_name)+trunc(salary/1000), '*')
    as "EMPLOYEES_AND_THEIR_SALARIES"
FROM employees
ORDER BY salary desc;

--13 DECODE 함수와 case 표현식을 사용해서  다음 표처럼 직무별로 grade를 출력하시오
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

--4 전체 사원 data중에서 . 월급의 최대값, 최소값, 합계, 평균을 출력하시오
--  컬럼 타이틀 Maximum, Minimum, Sum, Average
SELECT max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", avg(salary) "Average"
FROM employees;

--5 직무별 월급의 최대값, 최소값, 합계, 평균을 출력하시오 
--  컬럼 타이틀 Maximum, Minimum, Sum, Average
SELECT job_id, max(salary) "Maximum", min(salary) "Minimum", 
        sum(salary) "Sum", trunc(avg(salary)) "Average"
FROM employees
GROUP BY job_id
ORDER BY 1;

--6 직무별 사원수를 출력하시오
SELECT job_id, count(*)
FROM employees
GROUP BY job_id
ORDER BY 1;

--7 관리자인 사원의 수를 출력하시오
SELECT count(distinct manager_id) "Numer of Managers"
FROM employees; 

-- 8 Employees 사원중 최소 월급과 최대월급의 차이를 출력하시오
SELECT (max(salary) - min(salary)) "DIFFERENCE"
FROM employees;

--9 Employees 테이블 관리자가 없는 사원을 제외하고 관리자로 그룹핑된 
--  사원들(피관리자) 중에서 가장 낮은 월급을 받는 사원들의 최소급여가 
--  6000이상인 레코드를 최소급여의 내림차순으로 출력하시오
SELECT manager_id, min(salary)
FROM employees 
GROUP BY manager_id
HAVING manager_id is not null and min(salary) > 6000
ORDER BY 2 desc;

--10 전체 사원수, 1995, 1996, 1997, 1998년도에 입사한 사원수를 출력하시오
--   컬럼 타이틀은 total,  1995, 1996, 1997, 1998 로 출력하시오
SELECT count(*) "TOTAL" --비교하는 것. 그래서 decode나 case when 사용
    , sum(decode(to_char(hire_date, 'YYYY'),1995, 1, 0)) "1995"
    , sum(decode(to_char(hire_date, 'YYYY'),1996, 1, 0)) "1996"
    , sum(decode(to_char(hire_date, 'YYYY'),1997, 1, 0)) "1997"
    , sum(decode(to_char(hire_date, 'YYYY'),1998, 1, 0)) "1998"
FROM employees;

--11 직무별로 월급의 합계와   각 부서내에 직무별 월급의 합계를 아래 보기와 같이 출력하시오  
--   컬럼 타이틀은 Job, Dept 20, Dept 50, Dept 80, Dept 90로 출력하시오
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

--decode 사용
SELECT job_id,
       decode(department_id,20,sum_sal) "Dept 20",
       decode(department_id,50,sum_sal) "Dept 50",
       decode(department_id,80,sum_sal) "Dept 80",
       decode(department_id,90,sum_sal) "Dept 90", sum_sal "Total"
       FROM (SELECT job_id, department_id, sum(salary) sum_sal
             FROM employees 
             group by department_id, job_id);


--조인 연습문제-----------------------------------
--1 모든 사원의 소속 부서의 주소를 출력하시오
SELECT location_id, street_address, city, 
    state_province, country_id
FROM locations;

--2 사원들의 last_name과 부서번호와 부서이름을 출력하시오
SELECT e.last_name, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id;

--3 Toronto에서 근무하는 사원정보(last_name, 직무, 부서번호, 부서이름)를 출력하시오 
SELECT e.last_name, e.job_id, e.department_id, d.department_name
FROM employees e join departments d
    on e.department_id = d.department_id
    join locations l
    on d.location_id = l.location_id and
    l.city = 'Toronto';

--4 사원번호(last_name), 사원이름, 관리자번호, 관리자 이름(last_name)을 출력하시오
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a join employees b 
   on a.manager_id = b.employee_id
ORDER BY 4, 2;

--5 4번에서 관리자가 없는 King사원 데이터가 누락되었습니다.
--  관리자가 없는 King사원 데이터를 포함하여 사원번호(last_name), 
--  사원이름, 관리자번호, 관리자 이름(last_name)을 출력하시오
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 2;

--6 모든 사원에 대해서 동일한 부서에 근무하는 동료사원이름(last_name)을 
--  함께 출력하시오
SELECT a.last_name "Employee", a.employee_id "EMP#", 
    b.last_name "Manager", a.manager_id "Mgr#"
FROM employees a full outer join employees b 
   on a.manager_id = b.employee_id
ORDER BY 1;

--7 사원이름, 직무, 부서이름, 급여, 등급을 출력하시오
SELECT e.last_name, e.job_id, 
    d.department_name, e.salary, j.grade_level "gra"
FROM employees e  join departments d 
   on d.manager_id = e.manager_id
   join job_grades j 
   on e.salary
   between j.lowest_sal and j.highest_sal
ORDER BY 5;

--8 Davies. 사원 입사날짜 이후에 입사한 모든 사원의 이름과 입사날짜를 출력하시오
SELECT last_name, hire_date
FROM employees
WHERE hire_date > (SELECT hire_date  
                    FROM employees
                    WHERE last_name = 'Davies');

--9 사원들중에서 각사원의 관리자보다 먼저 입사한 사원들을 아래와 같이 출력하시오
SELECT e.last_name last_name, e.hire_date hire_date,
     m.last_name last_name, m.hire_date hire_date
FROM employees e, employees m
WHERE e.manager_id = m.employee_id
    and e.hire_date < m.hire_date;
