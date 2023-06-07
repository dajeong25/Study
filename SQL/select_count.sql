-- 프로그래머스 level 1, 조건에 맞는 회원수 구하기

-- EXTRACT, CAST
SELECT COUNT(*) AS "USERS"
FROM USER_INFO
WHERE EXTRACT(YEAR FROM CAST(JOINED AS DATE)) = '2021' AND AGE>=20 AND AGE<=29;

-- BETWEEN AND
SELECT COUNT(*) AS "USERS"
FROM USER_INFO
WHERE EXTRACT(YEAR FROM CAST(JOINED AS DATE)) = '2021' AND AGE BETWEEN 20 AND 29;

-- EXTRACT > 훨씬 간결
SELECT COUNT(*) AS "USERS"
FROM USER_INFO
WHERE EXTRACT(YEAR FROM JOINED) = 2021 AND AGE BETWEEN 20 AND 29;

-- BETWEEN AND, TO_DATE
SELECT COUNT(*) AS "USERS"
FROM USER_INFO
WHERE JOINED BETWEEN TO_DATE('20210101','YYYY-MM-DD') AND TO_DATE('20211231','YYYY-MM-DD')
    AND AGE BETWEEN 20 AND 29;
