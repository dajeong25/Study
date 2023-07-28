### 정규식
# grep('정규식', find_data) : find_data에서 '정규식'의 위치 리턴
# grep('정규식', find_data, value=T) : 일치하는 값을 리턴
char1 <- c("apple",'Apple','APPLE','banana','grape', 'apple2')
grep("apple", char1) #1

help(grep)

char2 = c('banana','apple')
grep(char2, char1) #4 : banana 문자열의 위치만 리턴
grep('banana|apple', char1) #1 4 : banana 또는 apple 문자열을 char1에서 위치 리턴
grep('banana|apple', char1, value=T) 
#"apple"  "banana" : banana 또는 apple 문자열을 char1에서 값을 리턴

# char1 데이터 요소 중 pp문자열을 가진 data의 위치를 출력
grep('pp', char1)

# char1 데이터 요소 중 pp 문자열을 가진 data를 출력
grep("pp", char1, value = T)

# char1 데이터 요소 중 대문자 A를 포함하는 문자 출력
grep("A", char1, value=T)

# char1 데이터 요소 중 a를 포함하는 문자 출력
grep("a", char1, value=T)

# char1 데이터 요소 중 A로 시작하는 문자 출력
grep("^A", char1, value=T)

# char1 데이터 요소 중 e를 포함하는 문자 출력
grep("e", char1, value=T)  #"apple"  "Apple"  "grape"  "apple2"

# char1 데이터 요소 중 e로 끝나는 문자 출력
grep("e$", char1, value=T)  #"apple"  "Apple"  "grape"

char3 <- c("apple1","apple",'Apple2','APPLE','banana','grape1', 'apple2')
# char3 데이터 요소 중 숫자를 포함하는 문자 출력
# 정규식 표현 : [] == 범위
#   숫자 표현 : [0-9] / [[:digit:]] / \d
#   [0-9] : 0에서 9사이의 문자
grep("[0-9]", char3, value=T) 
grep("[[:digit:]]", char3, value=T)
grep("\\d", char3, value=T)
#"apple1" "apple"  "grape1" "apple2"

# char3에서 2~5사이의 숫자를 포함하는 문자를 출력
grep("[2-5]", char3, value=T) #"Apple2" "apple2"

# Q. char3에서 대문자를 포함하는 문제 출력
grep("[A-Z]", char3, value=T)
grep("[[:upper:]]", char3, value=T)
# "Apple2" "apple2"

# Q. char3에서 소문자를 포함하는 문제 출력
grep("[a-z]", char3, value=T)
grep("[[:lower:]]", char3, value=T)
# "apple1" "apple"  "Apple2" "banana" "grape1" "apple2"

char4 <- c('홍길동','apple','가나다abc','가나다123','이 몽 룡','1234','!@#$','APPLE')
# 영문자를 포함하는 문자열 출력
grep("[A-Za-z]", char4, value=T)
grep("[A-z]", char4, value=T)
  # "apple"     "가나다abc" "APPLE"

# 문자를 포함하는 문자열
grep("[[:alpha:]]", char4, value=T)

# 문자, 숫자를 포함하는 문자열
grep("[[:alnum:]]", char4, value=T)

# 영문자, 숫자를 포함하는 문자열
grep("[A-z0-9]", char4, value=T)

# 한글를 포함하는 문자열
grep("[ㄱ-힣]", char4, value=T)

# 숫자로 끝나는 문자열
grep("[0-9]$", char4, value=T)
# 숫자 외에 문자를 포함하는 문자열
grep("[^0-9]", char4, value=T)
# 숫자로 시작하는 문자열
grep("^[0-9]", char4, value=T)

# 공백문자(space)를 포함하는 문자열
grep(" ", char4, value=T)
grep("\\s", char4, value=T)
grep("[[:blank:]]", char4, value=T)

# 공백문자를 포함하지 않는(non space) 문자열
grep("\\S", char4, value=T)

# 문자열의 +연산자 사용 안됨
'a' + 'b'

# paste : 문자열을 연결하여 하나의 문자열로 return
paste('a', 'b') #"a b"
paste('a', 'b', sep="")  #"ab"
paste('a', 'b', sep="-") #"a-b"
paste(char4, collapse = '-') #"홍길동-apple-가나다abc-가나다123-이 몽 룡-1234-!@#$-APPLE"
paste(char4, sep = '-') #"홍길동"    "apple"     "가나다abc" "가나다123" "이 몽 룡"  "1234"      "!@#$"      "APPLE" 

# substr(문자열, 시작인덱스, 종료인덱스) : 부분문자열
substr("abc123", 3,3) #c
substr("abc123", 1,3) #abc

# strsplit() : 하나의 문자열을 분리문자를 이용하여 여러개 문자열로 나눠 리턴
strsplit('2023/07/27', split='/') 
strsplit('2023-07-27', split='-') 
  #"2023" "07"   "27"  

