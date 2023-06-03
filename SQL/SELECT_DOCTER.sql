-- 흉부외과 또는 일반외과 의사 목록 출력하기
-- 프로그래머스 LEVEL 1

SELECT DR_NAME, DR_ID, MCDP_CD, TO_CHAR(HIRE_YMD, 'YYYY-MM-DD') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC;

-- 주의해야할 점 : 마지막 출력에서 날짜 변환이 다른 점 확인!
