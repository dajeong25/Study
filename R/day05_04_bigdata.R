#### 공기 오염 측정 데이터 분석
files <- c("airkorea/2015년1분기.csv","airkorea/2015년2분기.csv"
          ,"airkorea/2015년3분기.csv","airkorea/2015년4분기.csv"
          ,"airkorea/2016년 1분기.csv","airkorea/2016년 2분기.csv"
          ,"airkorea/2016년 3분기.csv","airkorea/2016년 4분기.csv")

ds <- NULL #ds데이터의 내용x 
for(f in files){
  print(f)
  tmp <- read.csv(f,header = T, fileEncoding = "cp949")
  ds <- rbind(ds,tmp)         #cp949 == euc-kr 동일한 인코딩
}
ds.copy <- ds #원본 저장
nrow(ds)
str(ds)

#측정소 지역 조회
unique(ds$지역)
head(ds,3)
names(ds)

#컬럼명 변경
ds <- rename(ds, loc=측정소코드, mdate=측정일시)
names(ds)
# 대기오염 요소
# so2  아황산가스
# co   일산화탄소
# o3   오존농도
# NO2  이산화질소
# PM10 미세먼지 10um이하
# PM25 초미세먼지 2.5um이하

# 해당열SO2의 결측값 개수
sum(is.na(ds[5])) #266360
# 해당열SO2의 결측값 비율
sum(is.na(ds[5])) / nrow(ds) #0.04760648
# 대기오염 요소에 해당하는 데이터의 결측값 개수와 비율 조회
for(i in 5:10){
  cat(names(ds)[i], sum(is.na(ds[i]))
      , sum(is.na(ds[i]))/nrow(ds), '\n')
}
  # SO2 266360 0.04760648 
  # CO 272901 0.04877555 
  # O3 253541 0.04531534 
  # NO2 213350 0.03813201 
  # PM10 436812 0.07807133 
  # PM25 3232418 0.5777295 

#PM25 컬럼의 결측값 비율이 0.5777295 정도 >> 너무 많음 >> 제거
ds <- ds[, -10]
str(ds)

# ds$year|month|hour : mdate에서 해당 년/월/시만 추출해서 각각 저장
# 1) mdate 자료형 : int -> str로 저장
mdate <- as.character(ds$mdate)
ds$year <- as.numeric(substr(mdate, 1, 4))
ds$month <- as.numeric(substr(mdate, 5, 6))
ds$hour <- as.numeric(substr(mdate, 9, 10))
str(ds)

# 서울 지역 측정소 번호
unique(ds$loc)
tmp <- subset(ds, subset=loc==111123) #loc==111123 종로구
tmp$측정소명
ds$locname[ds$loc==111123] <- "서울"
ds$locname[ds$loc==336111] <- "목포"
ds$locname[ds$loc==632132] <- "강릉"
str(ds)

#지역별locname 별로 미세먼지 분포도 박스그래프로
boxplot(PM10~locname, data=ds, main="미세먼지농도분포", ylim=c(1,120))

#결측값제거
ds <- ds[complete.cases(ds),] #46848 : locname의 결측값(서울,강릉,목포 그 외)도 다 사라져서
str(ds)
#년도별, 지역별, PM10 농도의 평균 조회
#aggregate >> groupby
tmp.year <- aggregate(ds$PM10, by=list(year=ds$year, loc=ds$locname), FUN="mean")
tmp.year

library(ggplot2)
ggplot(tmp.year, aes(x=year, y=x, colour=loc, group=loc))+
  geom_line()+
  geom_point(size=6, shape=19, alpha=0.5)+ #alpha: 투명도 (1불투명, 0투명)
  ggtitle("년도별 PM10 농도변화")+
  ylab("농도")

###########다시! 
folder = "airkorea"
setwd('D:/emspy/R/data')
files <- list.files(path=folder, pattern="csv$", full.names = TRUE)
files
ds <- NULL #ds데이터의 내용x 
for(f in files){
  print(f)
  tmp <- read.csv(f,header = T, fileEncoding = "cp949")
  ds <- rbind(ds,tmp)         #cp949 == euc-kr 동일한 인코딩
}
ds_copy <- ds #원본 저장

#pm25컬럼 제외
ds <- ds[, -10] 
str(ds) #5595037
ds <- ds[complete.cases(ds),]
str(ds) #4880982

#오염물질 간의 상관관계 조사(전수조사)
#산점도 출력
plot(ds, 5:9)  #시간이 너무 많이 걸림

##### 이럴때 필요한 것이 샘플링
# sample(데이터개수, 샘플데이터개수)
set.seed(1234)
sample <- ds[sample(nrow(ds), 5000), 5:9]
str(sample)
#산점도
plot(sample)
#상관계수 : a,b >> a변수가 1만큼 이동할 때, b변수가 0.8을 이동한다면, 상관계수=0.8
cor(sample)
# 미세먼지 최고값, 최저값
max(ds$PM10) #1238
which.max(ds$PM10) #158773
ds[which.max(ds$PM10),] #max값을 가진 데이터 전체 정보

min(ds$PM10) #0
which.min(ds$PM10) #313373
ds[which.min(ds$PM10),] #min값을 가진 데이터 전체 정보

max(ds$PM10); min(ds$PM10); which.min(ds$PM10); ds[which.min(ds$PM10),];
