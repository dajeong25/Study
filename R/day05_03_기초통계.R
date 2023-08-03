raincafe <- read.csv('cafedata.csv')
str(raincafe)

coffees = raincafe$Coffees #판매한 수량
min(coffees) #3 : 최소판매수량
sort(coffees)[1] 

max(coffees) #48: 최대판매수량
sort(coffees, decreasing=T)[1]

#최빈값 : 가장 많이 팔린 수량
table(coffees)
names(table(coffees))[which.max(table(coffees))] #4

#평균, 중앙값
mean(coffees) #21.51064
sum(coffees)  #1011
length(coffees) #47
median(coffees) #23
m <- (length(coffees)+1) %/% 2 #(47+1)/2 = 24
coffees.srt <- sort(coffees) #정렬
coffees.srt[m] #23 중앙값
# 요소의 개수 홀수 : 정렬한 데이터의 가운데값
# 요소의 개수 짝수 : 정렬한 데이터의 가운데값/2
a<-c(1,2,3,4)
median(a) #2.5

#표준편차 : 가운데값(평균)와 다른수와 차이의 제곱의 합의 평균의 제곱근
height <- c(164,166,168,170,172,174,176)

#평균
height.m <- mean(height)
height.m #170
height.dev <- (height - height.m)
height.dev #-6 -4 -2  0  2  4  6 : 평균값과의 차이
height.dev <- height.dev^2 #제곱
height.dev
sum(height.dev) #112 차이 제곱의 합
mean(height.dev) #16 분산. 편차 제곱의 평균
sqrt(mean(height.dev)) #4

#함수를 활용한 분산, 표준편차
var(height) #18.66667
s <- sum(height.dev) / (length(height)-1)
sqrt(s) #4.320494
sd(height)  #4.320494

# 사분위수 
qs <- quantile(coffees)
    # 0%  25%  50%  75% 100% 
    #  3   12   23   30   48 
print(qs[4]-qs[2]) #18 : 박스그래프의 상자 높이. 3분위수-1분위수
IQR(coffees) #18
