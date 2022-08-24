--1 Zlotkey사원과 같은 부서에 근무하는 사원 데이터 검색 (Zlotkey사원은 제외)
SELECT last_name, hire_date
FROM employees
WHERE department_id = (SELECT department_id
                    FROM employees
                    WHERE last_name = 'Zlotkey')
    and last_name != 'Zlotkey';

--2 전체 사원의 평균월급보다 월급을 많이 받는 사원 검색 (월급의 오름차순으로 정렬)
SELECT employee_id, last_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
                FROM employees)
ORDER BY 3;

--3 last_name에 'u' 문자가 포함되어 있는 사원들과 같은 부서에서 일하는 사원 검색
SELECT employee_id, last_name
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%');


--4 location ID 가 1700인 부서에 근무하는 사원 검색
SELECT e.last_name, e.department_id, e.job_id
FROM employees e, departments d
WHERE e.department_id = d.department_id 
    and d.location_id = 1700;

--서브쿼리 사용
select last_name, department_id, job_id
from employees
where department_id in (select department_id
                        from departments
                        where location_id = 1700)
order by 2, 3;


--5 King사원에게 직접 보고하는 모든 사원 검색(King사원을 관리자로 가지는 모든 사원 검색)
SELECT last_name, salary
FROM employees 
WHERE manager_id = (SELECT employee_id
                    FROM employees
                    WHERE last_name = 'King');

--6 'Executive' 부서에 근무하는 사원 검색
SELECT department_id, last_name, job_id
FROM employees 
WHERE department_id = (SELECT department_id
                    FROM departments
                    WHERE department_name = 'Executive');

--7 lastname에 'u'가 포함된 사원들과 같은 부서에 근무하면서 전체 사원의 
--  평균월급보다 월급을 많이 받는 사원 검색
SELECT employee_id, last_name, salary
FROM employees
WHERE department_id in (SELECT department_id
                    FROM employees
                    WHERE last_name like '%u%')
    AND salary > (SELECT avg(salary)
                FROM employees);
