### 종업원 팁 데이터 분석 : reshape2 패키지에 저장된 자료
# reshape2 패키지 설정
install.packages("reshape2") #reshape2 패키지 설치 - 하드웨어에 설치(딱 1번만 하면 됨)
library(reshape2) #설치된 패키지 중 사용 - 다음에는 이것만(import 느낌)
.libPaths() #패키지 어디 설치? 위치 반환

# 만약 폴더명에 한글이나 공백이 있으면 Error
# .libPaths(변경할 폴더) #패키지 설치 폴더 변경가능

class(tips)
str(tips)

#요일별 팀을 받은 개수 조회
table(tips$day)
  # Fri  Sat  Sun Thur 
  # 19   87   76   62 

#Dinner인 경우만 dinner에 저장
#Lunch인 경우만 lunch에 저장
dinner <- subset(tips, time == "Dinner")
lunch <- subset(tips, time == "Lunch")
str(dinner)
str(lunch)

# dinner 데이터에서 요일별 건수 조회
table(dinner$day)
  # Fri  Sat  Sun Thur 
  # 12   87   76    1 

# dinner 데이터에서 요일별 건수 조회
table(lunch$day)
  # Fri  Sat  Sun Thur 
  # 7    0    0   61 

#dinner, lunch 데이터에서 결제금액, 팁, 인원수의 평균 조회
colMeans(dinner[,c("total_bill", "tip", "size")])
  # total_bill        tip       size 
  # 20.797159   3.102670   
colMeans(lunch[c("total_bill", "tip", "size")])
  # total_bill        tip       size 
  # 17.168676   2.728088   2.411765

# 결제 금액 대비 팁의 비율 조회
tips$tip / tips$total_bill
# 결제 금액 대비 팁의 비율 평균 조회
mean(tips$tip / tips$total_bill) # 0.1608026
# 결제 금액 대비 팁의 비율 최대값조회
max(tips$tip / tips$total_bill)  # 0.7103448
# 결제 금액 대비 팁의 비율 최소값조회
min(tips$tip / tips$total_bill)  # 0.03563814

# 저녁시간의 결제금액 대비 팁의 비율 평균 조회
mean(dinner$tip / dinner$total_bill) #0.1595178
# 저녁시간의 결제금액 대비 팁의 비율 평균 조회
mean(lunch$tip / lunch$total_bill)   #0.1641279



##### 입력받기
install.packages('svDialogs')
library(svDialogs)
## BMI : 몸무게 / 미터환산 키의 제곱
# 25 미만 = 정상
# 25 이상 30미만 = 과체중
# 30이상 = 비만
bmi <- function(){
  height <- dlgInput("input height(cm)")$res
  weight <- dlgInput("input weight(kg)")$res
  w <- as.numeric(weight)
  h <- as.numeric(height)
  h = h/100
  BMI <- w/(h^2)
  if(BMI<25) cat(BMI, "정상")
  else if (BMI>=25 & BMI<30) cat(BMI, "과체중")
  else cat(BMI, "비만")
}
bmi()


### 파일로부터 데이터 입력받기
# airquality.csv파일을 다운받아 현재폴더/data/폴더에 넣기
getwd()
setwd("d:/emspy/R/data")
air <- read.csv("airquality.csv")
str(air)
head(air)

air <- read.csv("airquality.csv", header=T) #header 안 한 결과와 동일
str(air)
head(air, n=10)

#월별 레코드 건수 조회
table(air$Month)
  # 5  6  7  8  9 
  # 31 30 31 31 30

# 오존 수치별 레코드 건수 조회
table(air$Ozone)

table(is.na(air$Ozone)) #is.na() : 결측값 여부. 결측값 빈도수
  # FALSE(정상데이터)  TRUE(결측데이터)
  #       116           37 

table(!is.na(air$Ozone)) # ! == 결과 뒤집어서 보여줌
  # FALSE(결측데이터)  TRUE(정상데이터)
  #       37            116 

## 엑셀 파일 읽기
install.packages('xlsx')
library(xlsx) # rJava 패키지 필요 > 설치 후 path 설정
air <- read.xlsx("airquality.xlsx", header = T, sheetIndex = 1)
str(air)
# air$Ozone : 자료형 == char. why? NA를 문자열로 인식
table(is.na(air$Ozone))
table(is.na(air$Solar.R))

# Ozone, Solar.R 데이터 자료형을 숫자형으로 인식
# NA 결측값을 변환
air$Ozone <- as.numeric(air$Ozone)
air$Solar.R <- as.numeric(air$Solar.R)
str(air)

#air 데이터를 air.xlsx파일로 저장하기
write.xlsx(air, "air.xlsx", row.names=F)
