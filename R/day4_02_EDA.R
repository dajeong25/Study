### 데이터 전처리 : 결측값
z <- c(1,2,3,NA,5,NA,8)
# 벡터 데이터의 결측값 개수 출력
is.na(z)  # 결측값이면 TRUE
!is.na(z) # 정상값이면 TRUE
sum(is.na(z)) #2: 결측값 개수
sum(!is.na(z))#5: 정상값 개수

## 결측값 처리
# 1) 결측값을 0으로 치환
z1 <- z
z1[is.na(z)] <- 0
z1 #1 2 3 0 5 0 8
z  #1  2  3 NA  5 NA  8

# 2) 결측값 제거
z2 <- na.omit(z)    #결측값 제거
z2 <- as.vector(z2) #z2 객체를 벡터 객체로 변환
z2 <- as.vector(na.omit(z))
z2 #1 2 3 5 8


# ??? 놓침



x <- iris
x[3,2] <- NA
x[1,3] <- NA
x[5,3] <- NA
x[3,4] <- NA
head(x)

### x 데이터의 결측값 개수 조회
# 1) 열별 결측값 조회
# 반복문사용
for (i in 1:ncol(x)){  #ncol(x): x데이터 컬럼의 개수, 변수의 개수
  na <- is.na(x[i])
  cat(colnames(x)[i], '\t', sum(na), "\n")
}
# apply함수사용
cnt_na <- function(y){
  return(sum(is.na(y)))
}
apply(x, 2, cnt_na)

# colSums 함수 사용
na.cnt <- colSums(is.na(x))
na.cnt
  # Sepal.Length  Sepal.Width Petal.Length  Petal.Width  Species 
  #            0            1            2            1        0

# 2) 행별 결측값 개수 조회
na.cnt <- rowSums(is.na(x)) # 행별 결측값 개수
na.cnt 
na.cnt <- sum(rowSums(is.na(x))>0) #결측값 가지고 있는 행의 개수
na.cnt #3

# x 데이터에서 전체 결측값의 개수
sum(is.na(x)) #4

# x 데이터의 결측값을 0으로 치환
x[is.na(x)] <- 0
head(x)


x <- iris
x[3,2] <- NA
x[1,3] <- NA
x[5,3] <- NA
x[3,4] <- NA
head(x)

# x데이터에서 결측값을 가진 행만 y에 저장
# complete.cases(): NA값이 포함된 행(FALSE)은 제외하고 정상적인 데이터(TRUE)만 반환
y <- x[!complete.cases(x),]
y
  #   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
  # 1          5.1         3.5           NA         0.2  setosa
  # 3          4.7          NA          1.3          NA  setosa
  # 5          5.0         3.6           NA         0.2  setosa

# 결측값 제거된 행만 존재
x[complete.cases(x),]


### UN 데이터 분석
library(carData)
str(UN)
# 1. 열별 결측값 출력
colSums(is.na(UN))
  # region  group fertility ppgdp  lifeExpF  pctUrban  infantMortality
  #   14     14       14     14      14         14          6
# 2. lifeExpF 여성수명 평균 조회
mean(UN$lifeExpF[!is.na(UN$lifeExpF)]) #72.29319
mean(UN$lifeExpF, na.rm = TRUE)
# 3. 아시아 지역의 평균출산율 조회
mean(UN$fertility[which(UN$region=="Asia")], na.rm=TRUE) #2.43232
mean(UN[UN$region=="Asia","fertility"], na.rm=TRUE)
mean(UN[UN$region=="Asia",]$fertility, na.rm=TRUE)
mean(subset(UN, region=="Asia")$fertility, na.rm=TRUE)
# 4. 도시지역 평균과 영아사망률 평균 조회
colMeans(UN[,c('pctUrban', "infantMortality")], na.rm=TRUE)
  # pctUrban infantMortality 
  # 57.92965        29.43953 == NA : 값은 없지만, 자리수 존재.
tmp <- UN[,c('pctUrban', "infantMortality")]
colMeans(tmp[complete.cases(tmp),])
  # pctUrban infantMortality 
  # 57.10363        30.73905 == NA : 레코드 자체가 삭제 됨.
# >> 둘의 분모가 달라서 평균값이 달라짐


#### CES11 2011년도 캐나다 선거 통계 데이터
nrow(CES11) #2231
unique(CES11$abortion) #Levels: No Yes
# 낙태금지에 대한 찬성 반대 비율 조회
table(CES11$abortion)/nrow(CES11)
# 낙태금지에 대한 성별별 찬반 비율 조회
table(CES11$abortion[CES11$gender=='Male'])/nrow(CES11[CES11$gender=='Male',])
  #       No      Yes 
  # 0.816616 0.183384 
table(CES11$abortion[CES11$gender=='Female'])/nrow(CES11[CES11$gender=='Female',])
  #        No       Yes 
  # 0.8135048 0.1864952 

agg <- aggregate(CES11$abortion, by=list(CES11$gender), FUN=table)
agg
  #   Group.1 x.No x.Yes
  # 1  Female 1012   232
  # 2    Male  806   181

ncol(agg) #2
agg2 <- agg[,2]
agg2
  #        No Yes
  # [1,] 1012 232
  # [2,]  806 181

sum(agg2[1,]) #1244 : 여성의 인원수
sum(agg2[2,]) #987 : 남성의 인원수

agg2[1,] <- agg2[1,]/sum(agg2[1,])
agg2[2,] <- agg2[2,]/sum(agg2[2,])
rownames(agg2) <- agg[,1]
agg2
  #               No       Yes
  # Female 0.8135048 0.1864952
  # Male   0.8166160 0.1833840

#낙태금지에 도시지역, 비도시지역의 찬성/반대 비율 조회
agg <- aggregate(CES11$abortion, by=list(CES11$urban), FUN=table)
agg2 <- agg[,2]
rownames(agg2) <- agg[,1]
agg2[,1] <- agg2[1,]/sum(agg2[1,])
agg2[,2] <- agg2[2,]/sum(agg2[2,])
agg2
  #              No          Yes
  # rural 0.7517986 0.0009017368
  # urban 0.2482014 0.9990982632
