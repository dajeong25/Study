# 리스트
list1 <- list(name="James Seo", address="Seoul", tel='010-1111-2222', pay=500)
list1
  # $name
  # [1] "James Seo"
  # 
  # $address
  # [1] "Seoul"
  # 
  # $tel
  # [1] "010-1111-2222"
  # 
  # $pay
  # [1] 500

#name 값 조회
list1$name #"James Seo" : 데이터 값 리턴
list1[2:3] #2-3번째 데이터 조회.
  # address
  # [1] "Seoul"
  # 
  # $tel
  # [1] "010-1111-2222"$

#name, pay 값 조회
list1[c(1,4)]
  # $name
  # [1] "James Seo"
  # 
  # $pay
  # [1] 500

# Q. name = 홍길동, height:170인 리스트x 구현
x <- list(name="홍길동", height=170)

#조회
x[2] 
# $height
# [1] 170
x$score[2] #90

#추가
x$score <- c(80,90, 85)
x$birth <- "1990-01-01"
  # $name
  # [1] "김삿갓"
  # 
  # $height
  # [1] 170
  # 
  # $score
  # [1] 80 90 85
  # 
  # $birth
  # [1] "1990-01-01"

#수정
x$name <- '김삿갓'

# 삭제
x$birth <- NULL
  # $name
  # [1] "김삿갓"
  # 
  # $height
  # [1] 170
  # 
  # $score
  # [1] 80 90 85


# Q. name 값에 홍길동과 김삿갓 둘 다 저장
x$name[2] <- '홍길동'
x$name #"김삿갓" "홍길동"
