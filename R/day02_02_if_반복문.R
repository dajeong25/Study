#### if 구문
# if(조건식1) {
#   문장1 : 조건식1의 결과가 T인 경우 수행 문장
# } else if (조건식2) {
#   문장2 : 조건식1의 결과가 F & 조건식2의 결과가 T인 경우 수행 문장
# }
#   ....
# else {
#   모든 if, else if 의 결과가 F인 경우 수행되는 문장
# }

# Q. 입력된 숫자가 0보다 크면 2배 값을 리턴, 0보다 작으면 0을 리턴. 함수로 작성
#   >> 함수 : function | method | procedure | module
#   >> f(x)의 x == 파라미터, 인자, 매개변수
#   >> 조건문 내부에 문장이 한개인 경우 {} 생략 가능
f1 <- function(x){
  if(x>0) {
    return(x*2)
  } else{
    return(0)
  }
} 
f1(10)   #20
f1(-100) #100

# Q. 입력된 숫자가 0보다 크면 "양수", 0보다 작으면 "음수", 0이면 0을 리턴. 함수로 작성
f2 <- function(x){
  if(x>0)
    return("양수")
  else if(x==0)
    return(0)
  else
    return("음수")
}
f2(0)
f2(100)
f2(-20)

## ifelse(조건문, 참, 거짓) 구문 : 조건연산자
# Q. 점수가 60점 이상이면 합격, 아니면 불합격
score = 50
ifelse(score >= 60, "합격", "불합격")

#소문자, 대문자, 숫자인 경우 출력 > ASCii 코드 기준이라서 하나만 입력했을 때 가능
ch = "한글"
if(ch >= "A" & ch <= "Z") {"대문자" #'A' = 65
}else if(ch >= 'a' & ch <= 'z') {"소문자" #'a' = 97
}else if(ch >= '0' & ch <= '9') {"숫자" #'0' = 48
}else {'기타문자'}

# ascii 코드값 
charToRaw('A') #16진수 값

# strtoi() : 문자열을 정수형으로 변환.
# 16L : 16진수코드값 - 16진수로 인식 >> 정수 변환
strtoi(charToRaw('A'), 16L) #10진수로 출력

### 반복문 : for(변수 in 객체) {실행문장}
# Q. 1~10의 값을 출력
for (i in c(1:10)){
  print(i)
}
# Q. 1~10의 합 출력
hap = 0
for (i in c(1:10)){
  hap = hap + i
}
print(hap) #55


# Q. 1~100의 합 출력
hap = 0
for (i in c(1:100)){
  hap = hap + i
}
print(hap) #5050

# Q. 1~100 중에 짝수의 합만 출력
# A1
hap = 0
for (i in c(1:100)){
  if (i %% 2 == 0)
    hap = hap + i
}
print(hap) #2550

# A2 : i변수가 2~100 중 2씩 증가해서 변경
hap = 0
for (i in seq(2, 100, 2)){ 
    hap = hap + i
}
print(hap) #2550

## next - 반복문의 처음으로 제어 이동(continue와 동일한 기능)
hap = 0
for (i in c(1:100)){
  if (i %% 2 == 1) next
  hap = hap + i
}
print(hap) #2550

## break - 반복문 중지
# 1~100까지의 합을 구하는 중 100이 넘는 숫자 출력하기
hap = 0
for (i in c(1:100)){
  hap = hap + i
  if (hap > 100) break
}
cat(hap, i) #105 14

# Q1. 1~100 사이의 중에서 2의 배수이거나 3의 배수인 숫자의 합
hap = 0
for (i in c(1:100)){
  # if(i%%2==0) hap = hap + i
  # else if(i%%3==0) hap = hap + i
  if(i%%2==0 | i%%3==0) hap = hap + i
}
print(hap) #3417

# Q2. 1~100 사이의 중에서 2의 배수도 아니고 3의 배수도 아닌 숫자의 합
hap = 0
for (i in c(1:100)){
  # if(i%%2==0) next
  # else if(i%%3==0) next
  # else hap = hap + i
  if(i%%2!=0 & i%%3!=0) hap = hap + i
}
print(hap) #1633

## while(조건문) : 조건문의 결과가 참인 경우만 반복문 수행
i <- 0
while(i<5) {
  print(i)
  i <- i+1 
}
print(i)

# 1~100까지의 합을 구하는 중 100이 넘는 숫자 출력하기
i <- 0
hap <- 0
while (hap<100) {
  i <- i + 1
  hap = hap + i
}
cat(hap, i) #105 14 >> 정답

i <- 0
hap <- 0
while (hap<100) {
  hap = hap + i
  i <- i + 1
}
cat(hap, i) #105 15 >> i를 한 번더 더하고 나오기 때문에 +1이 됨


## Q. 500, 100, 50, 10 동전이 있다. 금액을 입력받아 동전으로 변경하는 함수 chgcoin 구현하라.
# 단, 동전의 개수는 최소한으로 한다.
# 벡터 객체로 500, 100, 50, 10 tjfwjd
# 금액 : 2580
# 500원 동전 : 5개
# 100원 동전 : 0개
# 50원 동전 : 1개
# 10원 동전 : 3개

chgcoin <- function(x){
  cat("금액 :", x ,"\n")
  
  ##반복문x
  a = x %/% 500
  cat("500원 동전 :", a, "개\n")
  b = (x %% 500) %/% 100
  cat("100원 동전 :", b, "개\n")
  c = (x %% 100) %/% 50
  cat("50원 동전 :", c, "개\n")
  d = (x %% 50) %/% 10
  cat("10원 동전 :", d, "개")
}

chgcoin <- function(x){
  cat("금액 :", x ,"\n")
  
  ## for 반복문
  for (c in c(500, 100, 50, 10)){
    cat(c, "원 동전 :", x%/%c, "개\n")
    x <- x%%c
  }
}

chgcoin <- function(x){
  cat("금액 :", x ,"\n")
  
  ## while 반복문
  coin <- c(500, 100, 50, 10)
  i <- 1
  while (x > 0){
    cat(coin[i], "원 동전 :", x%/%coin[i], "개\n")
    x <- x %% coin[i]
    i <- i+1
  }
}

### repeat : 그냥 계속 반복. break문이 필요함
chgcoin <- function(x){
  cat("금액 :", x ,"\n")
  coin <- c(500, 100, 50, 10)
  i <- 1
  repeat {
    cat(coin[i], "원 동전 :", x%/%coin[i], "개\n")
    x <- x %% coin[i]
    if(x <= 0) break
    i <- i+1
  }
}
chgcoin(2580)



# Q1)
# exam1 함수 : 매개변수 값이 5보다 크면 1리턴, 작으면 0리턴하는 함수
exam1 <- function(x){
  if(x>5) return(1)
  else return(0)
}

exam1 <- function(x){
  return(ifelse(x>5, 1, 0))
}
exam1(9)

# Q2)
# exam2 함수 : x,y 매개변수를 큰 수에서 작은수를 뺀 값을 리턴하는 함수
exam2 <- function(x, y){
  if (x > y) return(x-y)
  else return(y-x)
}
exam2 <- function(x, y){
  return (ifelse (x > y, x-y, y-x))
}
exam2(0,46)

# Q3)
# exam3 : 사과 10개를 한 바구니에 담는 다고 가정할 때, 
# 사과의 갯수를 매개변수로 입력받아 필요한 바구니 수를 리턴하는 함수
exam3 <- function(num){
  return(ifelse(num%%10==0, num%/%10, num%/%10+1))
}
exam3(10) #1
exam3(11) #2
exam3(101) #101

# Q4)
# exam4 : 1부터 매개변수로 입력받은 수까지의 전체합, 짝수, 홀수의 합을 출력하는 함수
exam4 <- function(end_num){
  odd <- 0
  even <- 0
  all_hap <- 0
  for(n in c(1:end_num)){
    all_hap = all_hap + n
    if(n%%2==0) even = even+n
    else odd = odd+n
  }
  cat(all_hap, even, odd)
}
exam4(10)  #55 30 25
exam4(100) #5050 2550 2500

