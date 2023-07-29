## 막대 그래프 barplot
f <- c('WINTER','SUMMER','SPRING','SUMMER','SUMMER','FALL','FALL','SUMMER','SPRING','SPRING')
ds <- table(f)
ds
barplot(ds, main='favorite season')
barplot(ds, main='favorite season', col='blue')
barplot(ds, main='favorite season', col=c('blue','red','green','cyan'))
barplot(ds, main='favorite season', col=rainbow(4))

# x,y축 설명
barplot(ds, main='favorite season', col=rainbow(4), xlab="계절", ylab="빈도수")
#수평막대그래프
barplot(ds, main='favorite season', col=rainbow(4), xlab="계절", ylab="빈도수", horiz=TRUE)
#이름변경하기
barplot(ds, main='favorite season', col=rainbow(4), xlab="계절", ylab="빈도수",
        horiz=TRUE, names=c("F", 'SP','SU','W'))
# x축의 이름 표시 방향 
# las=0 : 기본값, 축방향
# las=1 : 수평방향(가로)
# las=2 : 축 기준 수직
# las=3 : 수직방향(세로)
barplot(ds, main='favorite season', col=rainbow(4), xlab="계절", ylab="빈도수",
        horiz=TRUE, names=c("F", 'SP','SU','W'), las=1)

## 히스토그램 hist() : 자료의 분포 시각화
head(cars)
str(cars)

dist <- cars[,2]
hist(dist)
hist(dist, breaks=12) #breaks : 구간분리 개수
hist(dist, breaks=5)  #더 작게 하고 싶어도 시스템이 알아서 최소 구문을 분리함

h <- hist(dist, main="Histogram for 제동거리", xlab="제동거리", ylab="빈도수",
          border="blue", col="green", las=2, breaks=5)
h
# h$breaks : 구간 값
# h$counts : y축의 값. 빈도수값
# h$density : 구간별 밀도값
# h$mids : 구간의 중간값
# h$xname : 데이터의 이름
# h$equidist : 그래프의 간격이 일정한지 여부

# 구간별 빈도수 출력
freq <- h$counts
freq
names(freq) <- h$breaks[-1] # 제일 앞에 있는 0 제외
freq
  # 20  40  60  80 100 120 
  # 10  18  11   6   4   1

# 히스토그램에 빈도수 값 추가
# text(x좌표, y좌표, 표시할 값, 정렬방식)
# adj=c(0.5, -0.5) 정렬방식 == -1 ~ 1 사이값
  # 0 : 오른쪽정렬 / 0.5 : 가운데정렬 / 1 : 왼쪽정렬
  # 0 : 위쪽 / 0.5 가운데 / 1: 아래쪽
text(h$mids, h$counts, labels = h$counts, adj=c(0.5, -0.5)) 


###다이아몬드 시세를 히스토그램으로 표시
data("Diamonds")
str(Diamonds)
Diamonds$PricePerCt #캐럿당 가격

#캐럿당 가격을 히스토그램으로 출력
color <- rep('#a8dadc', 9)
color[3] <- '#1d3557'

hist(Diamonds$PricePerCt, main = "캐럿당 가격 분포", xlab="캐럿당 가격($)"
     , ylab="빈도수", col=color, las=1)


#R교재 - 310p : 하나의 화면에 여러 그래프 출력하기
# mfrow=c(2,2) : plot를 2행 2열로 분리. 4개의 그래프 출력
# mar=c(3,3,4,2) : margin 여백주기. [bottom, left, top, right]
par(mfrow=c(2,2), mar=c(3,3,4,2))
#1 히스토그램
hist(iris$Sepal.Length, main='Sepal.Length', col='Orange')
#2 막대그래프
barplot(table(mtcars$cyl), main='mtcars', col=c('red', 'green','blue'))
#3 막대그래프 > rainbow 팔레트 : 색상 모아놓은 객체
barplot(table(mtcars$gear), main='mtcars', col=rainbow(3), horiz=TRUE)
# 4 파이그래프 
# topo.colors : 팔래트
# radius : 반지름 
# radius=2 : 반지름을 2배로 
pie(table(mtcars$cyl), main="mtcars", col=topo.colors(3), radius = 0.8)
par(mfrow=c(1,1), mar=c(5,4,4,2)+.1)
str(mtcars)


## 3차원 그래프
install.packages('plotrix')

library(plotrix)
f <- c('WINTER','SUMMER','SPRING','SUMMER','SUMMER','FALL','FALL','SUMMER','SPRING','SPRING')
ds <- table(f) #도수분포
ds

# labelcex=1 : 출력 글자 크기
# explode=0.1 : 부채꼴 사이의 간격
pie3D(df, main='선호계절', labels=names(ds), labelcex=0.8
      , explode=0.05, col=rainbow(4), radius = 0.8)

### plot 선그래프
# plot(x축 데이터, y축 데이터)
# type="o" : 선의 종류 [l,b,s,o]
# 
month = 1:12
late = c(5,8,7,9,4,6,12,13,8,6,6,4)
plot(month, late, type="s", lty=6, lwd=2, xlab='Month', ylab="Late cnt")
plot(month, late, type="b", lty=6, lwd=2, xlab='Month', ylab="Late cnt")
plot(month, late, type="o", lty=6, lwd=2, xlab='Month', ylab="Late cnt")
plot(month, late, type="l", lty=6, lwd=2, xlab='Month', ylab="Late cnt")


## boxplot : 상자그래프
hist(cars$dist)
boxplot(cars$dist, main="제동거리")

#수치정보
boxplot.stats(cars$dist)
  # $stats
  # [1]  2 26 36 56 93
  #  2 = 최소값
  # 26 = 제1사분위값(Q1). 25%에 해당하는 값
  # 36 = 중간값. 50%에 해당하는 값
  # 56 = 제3사분위값(Q3). 75%에 해당하는 값
  # 93 = 최대값. 특이값 제외
  # 
  # $n : 현재 관측값의 개수
  # [1] 50 
  # 
  # $conf : 중간값에 대한 신뢰구간
  # [1] 29.29663 42.70337
  # 
  # $out : 특이값(이상치)
  # [1] 120

#그룹이 있는 boxplot
boxplot(Petal.Length~Species
        , data=iris
        , main="품종별 꽃잎의 길이"
        , col=c('green', 'yellow','blue'))

boxplot(iris$Petal.Length~iris$Species #data= : 입력하지 않으면 명시 필수
        , main="품종별 꽃잎의 길이"
        , col=c('green', 'yellow','blue'))


#mtcars 데이터의 mpg값을 상자그래프로 출력
boxplot(mtcars$mpg, main='mpg')
boxplot.stats(mtcars$mpg)
  # $stats
  # [1] 10.40 15.35 19.20 22.80 33.90
  # 
  # $n
  # [1] 32
  # 
  # $conf
  # [1] 17.11916 21.28084
  # 
  # $out
  # numeric(0)

#gear 기어의 수에 따른 자동차들의 연비 값을 상자그래프로 출력
levels(factor(mtcars$gear)) #"3" "4" "5" : gear의 값의 종류
boxplot(mtcars$mpg~mtcars$gear, col=rainbow(3), main="기어별 연비")

# gear==4인 데이터의 연비를 그리기
boxplot(subset(mtcars, gear==4)[,"mpg"], main="4기어의 연비", ylab="연비")
boxplot(mtcatrs$mpg[which(mtcars$gear==4)], main="4기어의 연비", ylab="연비")
boxplot.stats(mtcars$mpg[which(mtcars$gear==4)])
  # $stats
  # [1] 17.80 21.00 22.80 28.85 33.90
  # 
  # $n
  # [1] 12
  # 
  # $conf
  # [1] 19.21956 26.38044
  # 
  # $out
  # numeric(0)

# am 변속기의 종류 값에 따른 연비
boxplot(mtcars$mpg~mtcars$am, main="변속기 종류에 따른 연비", col=c('blue','yellow'))

# 중량 wt이 평균이상인 그룹high과 미만인 그룹low으로 나눠 grp에 저장
grp = rep('high', nrow(mtcars)) #벡터생성
grp[mtcars$wt < mean(mtcars$wt)] = 'low'
grp
  #  [1] "low"  "low"  "low"  "low"  "high" "high" "high" "low"  "low"  "high" "high" "high"
  # [13] "high" "high" "high" "high" "high" "low"  "low"  "low"  "low"  "high" "high" "high"
  # [25] "high" "low"  "low"  "low"  "low"  "low"  "high" "low"
boxplot(mtcars$hp~grp)

# 위의 그룹에서 연비mpg 분포 출력
boxplot(mtcars$mpg~grp)
