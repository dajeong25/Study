##### DML : 데이터 조작어  ######
# Data Manipulation Language
-- INSERT : 레코드 추가
		# insert into 테이블명 (컬럼명1, 컬럼명2, --)
		# values(값1, 값2, ...)
-- UPDATE : 레코드의 컬럼 값을 수정
		# update 테이블명 set 컬럼명=값1, 컬럼명2=값2,...
		# where 레코드 선택 조건
-- DELETE : 레코드 삭제
		# delete from 테이블명 where 레코드 선택 조건
-- SELECT : 테이블의 내용 조회
		# select 컬럼명1, 컬럼명2, ... | *(모든컬럼)
		# from 테이블명
		# where 레코트 선택 조건
		# group by 컬럼명 
		# having 그룹함수조건
		# order by 컬럼명 [asc/desc] >> sorting

-- C : create, insert
-- R : read , select 
-- U : update, update
-- D : delete, delete

# 학생 테이블 생성
CREATE table student(
	studno INT PRIMARY KEY,
	NAME VARCHAR(20) NOT NULL,
	grade INT ,
	major VARCHAR(50)
);

# student 테이블의 데이터 조회
SELECT * FROM student;

# student table에 데이터 추가
INSERT INTO student (studno, NAME, grade, major)
VALUES (1,'홍길동',1,'경영');

SELECT * FROM student;

INSERT INTO student (studno, NAME, grade, major)
VALUES (2,'이몽룡',2,'무역');
INSERT INTO student (studno, NAME, grade, major)
VALUES (3,'김삿갓',3,'컴공');

SELECT * FROM student;

# student 테이블의 이름과 학년만 조회
SELECT NAME, grade FROM student;

# student 테이블의 2학년 학생의 모든 컬럼 조회
SELECT * FROM student WHERE grade = 2;

# student 테이블의 2학년 학생의 이름, 전공 컬럼만 조회
SELECT NAME, major FROM student WHERE grade = 2;

SELECT NAME, major FROM student WHERE 1=1; -- 무조건 전체 출력
SELECT NAME, major FROM student WHERE 1=2; -- 무조건 아무것도 출력x

# 수정 : 홍길동 학생의 정보를 전공:회계, 학년:1으로 바꿔보자
UPDATE student SET major='회계', grade=2
WHERE NAME='홍길동';

SELECT * FROM student;

#삭제 : 김삿갓 학생을 학생정보에서 제거하기
#       레코드 삭제
DELETE FROM student WHERE NAME='김삿갓';
SELECT * FROM student;

# 이름으로 정렬
SELECT * FROM student ORDER BY NAME DESC;

SET autocommit = FALSE;
INSERT INTO student (studno, NAME, grade, major)
VALUES (3,'김삿갓',3,'컴공');
COMMIT;

DELETE FROM student WHERE studno=3;
ROLLBACK;

#### TCL : DCL의 일부 ####
# Transaction Control Language
# Transaction 트랜젝션 : 업무단위
# DML 명령어에서만 가능!
-- commit : 결과 물리적인 저장 공간에 저장
-- rollback : 수정된 내용 취소
-- 둘 다 트랜젝션을 종료하는 제어어
UPDATE student SET NAME='가가가';
SELECT * FROM student;
ROLLBACK;


#### DDL : 데이터 정의어 ####
# Data Definition Language
-- CREATE : 객체 생성 
		# CREATE TABLE 테이블명 (컬럼명1, 컬럼명2, ..)
-- ALTER : 객체의 구조 변경
		# ALTER TABLE 테이블명 조건
-- DROP : 객체 제거
		# drop tabel 테이블명
		
ALTER TABLE student ADD major2 VARCHAR(50);
SELECT * FROM student;

DROP TABLE student; # autocommit!! 
ROLLBACK; # rollback이 안 됨! 정말 조심해야함!
