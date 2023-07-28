### 이전 복습
# 1. 콘솔 출력
#   print(1+2) : 1개만 출력
#   cat(1,2)   : 2개이상 출력
#   
# 2. 연산자
#    /  : 나누기
#   %/% : 정수 나누기
#   %%  : 나머지
#   ^, ** : 제곱
# 
# 3. 함수
#   as.numeric(문자열) : 숫자로된 문자열을 숫자로 변경
#   as.Date('날짜') : 날짜형 문자열을 날짜로 변경
#   Sys.Date() : 오늘 날짜
#   Sys.time() : 오늘 시간
#   date()     : 현재 일시. 출력형식이 영어권 기준
#   
# 4. Data objects : 데이터 모임
#   - vector     : 데이터를 1차원 형태로 저장하는 객체
#                   c(1,2,3) / 1:3 / seq(1,10,2) / rep(1:3, 2)
#   - factor     : 범위를 가진 벡터의 일종
#   - list       : 딕셔너리 형태
#   - matrix     : 2차원 배열
#   - data.frame : 표 형태의 데이터
#   - array      : 일반적으로 3차원 이상의 데이터 표현
# 
# 5. 데이터 자료형
#   - 숫자형: numeric() 정수(integer), 실수(double), 복소수(complex)
#   - 문자형: character(), "aaa", 'aaa'
#   - 논리형: logical(), TRUE(T,1), FALSE(F, 0)
#   - 날짜형: date(). 내부적으로는 numeric, 외부적으로는 문자형으로 출력됨
# 
# 6. 집합
#   - 합집합: union()
#   - 교집합: intersect()
#   - 차집합: setdiff()

###### merge #######
# merge(병합) : 두 개의 데이터프레임을 합하는 기능. 컬럼을 기준으로 데이터 병합
  # merge(A, B): 컬럼명의 값이 같은 데이터만 병합
  # merge(A, B, by="key컬럼"): merge의 key값이 같은 데이터만 병합 [inner join]

cust_id <- c("c01","c02","c03","c04","c05","c06","c07")
last_name <- c("Kim","Lee","Choi","Park","Bae","Kim","Lim")
cust1 <- data.frame(cust_id, last_name)
cust1
  #   cust_id last_name
  # 1     c01       Kim
  # 2     c02       Lee
  # 3     c03      Choi
  # 4     c04      Park
  # 5     c05       Bae
  # 6     c06       Kim
  # 7     c07       Lim

cust2 <- data.frame(cust_id=c("c05","c06","c07","c08","c09")
                    , last_name=c("Bae","Kim","Lim2","Cho","Yoo"))
cust2
  #   cust_id last_name
  # 1     c05       Bae
  # 2     c06       Kim
  # 3     c07       Lim
  # 4     c08       Cho
  # 5     c09       Yoo

cust3 = merge(cust1, cust2)
cust3
  #   cust_id last_name
  # 1     c05       Bae
  # 2     c06       Kim

cust3 = merge(cust1, cust2, by="cust_id")
cust3
  #   cust_id last_name.x last_name.y
  # 1     c05         Bae         Bae
  # 2     c06         Kim         Kim
  # 3     c07         Lim        Lim2


# [full outer join] : merge(A, B, by="key컬럼", all=TRUE) key를 기준으로 모든 데이터 병합
cust4 = merge(cust1, cust2, by="cust_id", all=TRUE)
cust4
  #   cust_id last_name.x last_name.y
  # 1     c01         Kim        <NA>
  # 2     c02         Lee        <NA>
  # 3     c03        Choi        <NA>
  # 4     c04        Park        <NA>
  # 5     c05         Bae         Bae
  # 6     c06         Kim         Kim
  # 7     c07         Lim        Lim2
  # 8     c08        <NA>         Cho
  # 9     c09        <NA>         Yoo

# [left outer join] : merge(x=A, y=B, by="key컬럼", all.x=TRUE) key를 기준으로 모든 x데이터만 병합
cust5 = merge(cust1, cust2, by="cust_id", all.x=TRUE)
cust5
  #   cust_id last_name.x last_name.y
  # 1     c01         Kim        <NA>
  # 2     c02         Lee        <NA>
  # 3     c03        Choi        <NA>
  # 4     c04        Park        <NA>
  # 5     c05         Bae         Bae
  # 6     c06         Kim         Kim
  # 7     c07         Lim        Lim2

# [right outer join] : merge(x=A, y=B, by="key컬럼", all.y=TRUE) key를 기준으로 모든 y데이터만 병합
cust6 = merge(cust1, cust2, by="cust_id", all.y=TRUE)
cust6
  #   cust_id last_name.x last_name.y
  # 1     c05         Bae         Bae
  # 2     c06         Kim         Kim
  # 3     c07         Lim        Lim2
  # 4     c08        <NA>         Cho
  # 5     c09        <NA>         Yoo

### rbind : dataframe 행추가하기(concat과 동일)
df1 = data.frame(name=c('apple', 'banana','cherry'), price=c(300,200,100))
df1
  #     name price
  # 1  apple   300
  # 2 banana   200
  # 3 cherry   100

# 행추가
df2 <- data.frame(name=c('mango','berry'), price=c(400, 500))
df1 <- rbind(df1, df2)
df1
  #     name price
  # 1  apple   300
  # 2 banana   200
  # 3 cherry   100
  # 4  mango   400

# 열추가. 행 수가 같아야함
df1 <- cbind(df1, data.frame(qty=c(10,20,30,40,50)))
df1
  #     name price
  # 1  apple   300
  # 2 banana   200
  # 3 cherry   100
  # 4  mango   400
  # 5  berry   500

### subset(data, select=컬럼명|vector) : 부분 데이터만 리턴
no <- c(1,2,3,4,5)
name <- c('서진수','주시현','최경우','이동근','윤정웅')
address <- c('서울','대전','포항','경주','경기')
tel <- c(1111,2222,3333,4444,5555)
hobby <- c("독서","미술","여행","요리","운동")
member <- data.frame(NO=no, NAME=name, ADDRESS=address, TEL=tel, HOBBY=hobby)
member
  #   NO   NAME ADDRESS  TEL HOBBY
  # 1  1 서진수    서울 1111  독서
  # 2  2 주시현    대전 2222  미술
  # 3  3 최경우    포항 3333  여행
  # 4  4 이동근    경주 4444  요리
  # 5  5 윤정웅    경기 5555  운동

#번호, 이름, 전화번호만 저장
member2 <- subset(member, select=c(NO,NAME,TEL))
member2
  #   NO   NAME  TEL
  # 1  1 서진수 1111
  # 2  2 주시현 2222
  # 3  3 최경우 3333
  # 4  4 이동근 4444
  # 5  5 윤정웅 5555

# 취미만 제외
member3 <- subset(member, select=-HOBBY)
member3
  #   NO   NAME ADDRESS  TEL
  # 1  1 서진수    서울 1111
  # 2  2 주시현    대전 2222
  # 3  3 최경우    포항 3333
  # 4  4 이동근    경주 4444
  # 5  5 윤정웅    경기 5555

# 컬럼명 변경 >> col.names는 Error
colnames(member3) = c('번호','이름','주소','전화번호')
member3[1:3,]
  #   번호   이름 주소 전화번호
  # 1    1 서진수 서울     1111
  # 2    2 주시현 대전     2222
  # 3    3 최경우 포항     3333

# 역순으로 지정 조회
member3[c(5,4),]
  # 번호   이름 주소 전화번호
  # 5    5 윤정웅 경기     5555
  # 4    4 이동근 경주     4444