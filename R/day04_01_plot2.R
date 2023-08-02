#### 산점도 : 두 변수 사이의 관계파악에 사용되는 그래프
str(mtcars)
# mtcars$wt : 자동차 무게 데이터, x축
# mtcars$mpg: 자동차 연비 데이터, y축
# pch=19    : 점의 모양. 1~25
plot(mtcars$wt, mtcars$mpg,main='중량-연비 그래프'
     , xlab = '중량', ylab='연비(MPG)', pch=20)

# 여러 변수들간의 산점도 pairplot
vars <- c("mpg", 'disp','drat','wt')
target = mtcars[vars]
plot(target, main='여러변수들 간의 산점도')

# 그룹 정보가 있는 2개의 변수
str(iris)
iris2 <- iris[,3:4]
iris2
group = as.numeric(iris$Species) 
levels(iris$Species)
  # 종류를 level 순소대로 숫자형태로 변경됨
group

color <- c('red','blue','green')
plot(iris2, main='품종별 꽃잎의 길이와 넓이',col=color[group], pch=c[group])
#범례
legend(x='bottomright', legend=levels(iris$Species), col=color, pch=c(1:3))


#### 353p 자동차 선팅 데이터
install.packages("DAAG")
library(DAAG)
str(tinting)
   # $ tint(선팅정도) : Ord.factor w/ 3 levels "no"<"lo"<"hi": 1 2 3 1 ...
   # $ it  (식별시간) : num  26 32.2 27 17.7 20.8 ...
   # $ csoa(문자인식시간) : num  46.8 37.4 42.6 41.6 37.4 ...
plot(tinting$it, tinting$csoa)
group = as.numeric(tinting$tint)
group
plot(tinting$it, tinting$csoa, pch=c(group), col=color[group])
legend(x='bottomright', legend=levels(tinting$tint), col=color, pch=c(1:3))

  # $ agegp : Factor w/ 2 levels "younger","older": 1 1 1 ...
group = as.numeric(tinting$agegp)
plot(tinting$it, tinting$csoa, pch=c(group), col=color[group])
legend(x='bottomright', legend=levels(tinting$agegp), col=color, pch=c(1:2))


#### 서울 온도 데이터
setwd("d:/emspy/R/data")
getwd()
df = read.csv('seoul_temp_2017.csv')
str(df)
  # 'data.frame':	365 obs. of  3 variables:
  #  $ date    : chr  "2017-01-01" "2017-01-02" ...
  #  $ month   : int  1 1 1 1 1 1 1 1 1 1 ...
  #  $ avg_temp: num  2.7 5 2 3.9 3.8 5.4 ...

boxplot(df$avg_temp, col='green', ylim=c(-20,40), xlab='서울 1년 기온'
        , ylab='평균기온')
summary((df$avg_temp))
    #  Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    # -9.40    3.00   15.10   13.07   22.60   31.40 

#월별 평균기온
# agrregate(원본데이터, by=그룹데이터, 적용함수)
list(df$month)
month.avg <- aggregate(df$avg_temp, by=list(df$month), mean)
  #    Group.1          x
  # 1        1 -1.8290323
  # 2        2 -0.2464286
  # 3        3  6.3258065
  # 4        4 13.9333333
  # 5        5 19.4903226
  # 6        6 23.2733333
  # 7        7 26.9225806
  # 8        8 25.9161290
  # 9        9 22.1033333
  # 10      10 16.4096774
  # 11      11  5.6266667
  # 12      12 -1.9290323
month.avg <- month.avg[,2] #온도평균값
names(month.avg) <- 1:12
month.avg
  #          1          2          3          4          5          6          7          8 
  # -1.8290323 -0.2464286  6.3258065 13.9333333 19.4903226 23.2733333 26.9225806 25.9161290 
  #          9         10         11         12 
  # 22.1033333 16.4096774  5.6266667 -1.9290323 

# 평균기온 역순위(내림차순) 정렬 시 순위(높은온도:7월=1위)
ord <- rank(-month.avg) #내림차순 정렬하여 순위
ord # 평균온도가 높은 순서
  #  1  2  3  4  5  6  7  8  9 10 11 12 
  # 11 10  8  7  5  3  1  2  4  6  9 12 

#avg_temp~month : avg_temp데이터를 month로 그룹화
boxplot(avg_temp~month, data=df, col=heat.colors(12)[ord]
        , ylim=c(-20,40), ylab="기온", xlab="월", main="서울시 월별 기온 분포(2017")

#### 월별 평균 오존 농도 계산
airquality
str(airquality) #'data.frame':	153 obs. of  6 variables
month.avg <- aggregate(airquality$Ozone, by=list(airquality$Month), mean)
month.avg
  #   Group.1  x
  # 1       5 NA
  # 2       6 NA
  # 3       7 NA
  # 4       8 NA
  # 5       9 N
  # 결과가 NA : 결측값과 연산시 결과는 결측값
#airqulity에서 결측값 제거.
complete.cases(airquality)
  # TRUE : 결측값 없음, FALSE: 결측값 있음
ds <- airquality[complete.cases(airquality),]
str(ds) #'data.frame':	111 obs. of  6 variables
month.avg <- aggregate(ds$Ozone, by=list(ds$Month), mean)
month.avg <- month.avg[,2]
names(month.avg) <- unique(ds$Month)
month.avg
  # 5        6        7        8        9 
  # 24.12500 29.44444 59.11538 60.00000 31.44828 

#오존 농도 순위를 내림차순으로 정렬하여 순위값 조회
ord <- rank(-month.avg)
ord
  # 5 6 7 8 9 
  # 5 4 2 1 3 
#박스그래프로 작성
boxplot(Ozone~Month, data=ds, col=heat.colors(5)[ord], ylim=c(0,170)
        , ylab="오존농도", xlab="월", main="월별 오존농도")

# ggplot 패키지를 위한 시각화 : 그래프와 데이터 종류가 분리
install.packages("ggplot2")
library(ggplot2)
#꽃잎의 길이를 히스토그램으로 출력
ggplot(iris, aes(x=Petal.Length)) + geom_histogram()
#데이터 간격
ggplot(iris, aes(x=Petal.Length)) + geom_histogram(binwidth = 0.5)
#품종정보로 꽃받침의 폭을 히스토그램으로 출력
# position = 'dodge' : 막대를 품종별로 분리
ggplot(iris, aes(x=Sepal.Width, fill=Species, color=Species)) + 
  geom_histogram(binwidth = 0.5, position = 'dodge')+ 
  theme(legend.position = 'top')
ggplot(iris, aes(x=Sepal.Width, fill=Species, color=Species)) + 
  geom_histogram(binwidth = 0.5)+ 
  theme(legend.position = 'top')

#geom_point() : 산점도 그래프 작성
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width)) +
  geom_point(size=3)

#품종별로 다른 색상 지정하기
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, color=Species))+
  geom_point(size=2) #size= : 점의 크기

#제목 지정
ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, color=Species))+
  geom_point(size=2) + ggtitle("iris 꽃잎의 길이와 폭") +
  theme(plot.title=element_text(size=25, face="bold", colour='steelblue'))

#geom_boxplot : 상자그래프
ggplot(data=iris, aes(y=Petal.Length))+geom_boxplot(fill='yellow')

#품종별 꽃잎의 길이를 상자 그래프로 출력
ggplot(data=iris, aes(y=Petal.Length, x=Species,fill=Species))+
  geom_boxplot()

#geom_line() : 선그래프
str(airmiles) # 1937~1960년까지 항공기 승객들의 이동거리 통계
year <- 1937:1960
cnt <- as.vector(airmiles)
df <- data.frame(year, cnt)
head(df)
  #   year  cnt
  # 1 1937  412
  # 2 1938  480
  # 3 1939  683
  # 4 1940 1052
  # 5 1941 1385
  # 6 1942 1418
ggplot(data=df, aes(x=year, y=cnt)) + geom_line(color='red')

#geom_bar() : 막대그래프
# 1. 월별 평균기온
df <- aggregate(airquality$Temp, by=list(month=airquality$Month), mean)
df
  #   month        x
  # 1     5 65.54839
  # 2     6 79.10000
  # 3     7 83.90323
  # 4     8 83.96774
  # 5     9 76.90000

ggplot(df, aes(x=month, y=x)) + 
  # stat='identity': 필수 기입(데이터임을 알려줌)
  geom_bar(stat='identity', width=0.7, fill='red')

# 월별 오존 농도를 상자 그래프를 작성
ggplot(data=airquality, aes(x=factor(Month), y=Ozone, fill=factor(Month)))+geom_boxplot()
  # Warning message:
  #   Removed 37 rows containing non-finite values (`stat_boxplot()`). 
  # 그래도 그래프는 그려줌
#결측값 제거
df<- airquality[complete.cases(airquality),]
ggplot(data=df, aes(x=factor(Month), y=Ozone, fill=factor(Month)))+geom_boxplot()

#기온과 오존 농조로 산점도 출력하기
ggplot(data=df, aes(x=Temp, y=Ozone))+geom_point(size=3,color='orange')
ggplot(data=df, aes(x=Temp, y=Ozone,colour='orange'))+geom_point(size=3)
## 중위값과 평균의 1위가 다름

#7월의 일별 오존농도를 선그래프로 출력
df7 <- subset(df, Month==7)
# df7 <- df[df$Month ==7,]
# df7 <- df[which(df$Month==7),]

unique(df7$Month)
unique(df7$Day)

ggplot(data=df7, aes(y=Ozone, x=Day))+geom_line(col='red')


#### carData 패키지의 UN98 데이터셋 분석
install.packages('carData')
library(carData)
data(UN98)
summary(UN98)
str(UN98)
# region : 대륙
# tfr    : 출산율
unique(UN98$region) #Asia Europe Africa America Oceania
table(is.na(UN98$tfr))
  # FALSE  TRUE 
  #   197    10 

#대륙별 평균출산율을 막대그래프로 출력
df <- UN98[, c('region','tfr')]
df <- df[complete.cases(df),]
df <- aggregate(df[,'tfr'], by=list(region=df$region), mean)
df
  #    region        x
  # 1  Africa 5.250741
  # 2 America 2.837297
  # 3    Asia 3.729796
  # 4  Europe 1.613171
  # 5 Oceania 3.609375

ggplot(data=df, aes(x=region, y=x))+
  geom_bar(stat='identity', width=0.7, fill=rainbow(5))

# educationMale  : 남성의 교육 수준
# educationFemale: 여성의 교육 수준
# 남여의 교육수준을 산점도로 출력하되, 대륙별 다른 색상으로.
df <- UN98[,c('region','educationMale','educationFemale')]
str(df)
  # 'data.frame':	207 obs. of  3 variables:
  #  $ region         : Factor w/ 5 levels..: 3 4 1...
  #  $ educationMale  : num  NA NA 11.1 NA NA ...
  #  $ educationFemale: num  NA NA 9.9 NA NA NA NA ...
df <- df[complete.cases(df),]
str(df) #'data.frame':	76 obs. of  3 variables
ggplot(data=df, aes(x=educationMale, y=educationFemale, color=region))+
  geom_point(size=2)


###방사형 차트
install.packages('fmsb')
library(fmsb)
score <- c(80,60,95,85,40)
max_score <- rep(100, 5)
min_score <- rep(0, 5)
ds <- rbind(max_score, min_score, score)
ds <- data.frame(ds)
colnames(ds) <- c('국어','영어','수학','물리','음악')
ds
  #           국어 영어 수학 물리 음악
  # max_score  100  100  100  100  100
  # min_score    0    0    0    0    0
  # score       61   61   95   80   61

radarchart(ds, pcol='dark green', pfcol=rgb(0.2,0.5,0.5,0.5)
           , plwd=3, cglcol='grey', cglwd=0.8, cglty=1, seg=4
           , axistype=1, seg=4, axislabcol='grey', caxislabels=seq(0,100,25))

## 종교 유무 조사

