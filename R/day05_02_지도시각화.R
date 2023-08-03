## 지도시각화
install.packages("ggiraphExtra") #지도 관련 패키지
install.packages("mapproj")      #ggiraphExtra 패키지에서 필요한 패키지
library(ggiraphExtra)

# 미국 주별 강력 범죄율
str(USArrests)
head(USArrests, 3)
  #            Murder Assault UrbanPop Rape
  # Alabama      13.2     236       58 21.2
  # Alaska       10.0     263       48 44.5
  # Arizona       8.1     294       80 31.0

# USArrests 데이터 행 이름을 state 컬럼으로 변경
library(tibble)
crime <- rownames_to_column(USArrests, var="state")
head(crime, 3)
  #     state Murder Assault UrbanPop Rape
  # 1 Alabama   13.2     236       58 21.2
  # 2  Alaska   10.0     263       48 44.5
  # 3 Arizona    8.1     294       80 31.0

library(ggplot2)
states_map <- map_data("state") #위도 경도 값 내포
head(states_map, 3)
  #        long      lat group order  region subregion
  # 1 -87.46201 30.38968     1     1 alabama      <NA>
  # 2 -87.48493 30.37249     1     2 alabama      <NA>
  # 3 -87.52503 30.37249     1     3 alabama      <NA>
nrow(states_map) #15537

#states_map 정보와 crime의 state 정보와 일치시킴
# tolower() : 소문자로 변경
crime$state <- tolower(crime$state)
crime$state

#지도출력
ggChoropleth(data=crime        #지도에 표시할 데이터
             , aes(fill=Murder #표시할 컬럼값
                   , map_id=state) #지도에 표시할 컬럼값
             , map=states_map) #지도 데이터, 위도 경도 값

ggChoropleth(data=crime        #지도에 표시할 데이터
             , aes(fill=Murder #표시할 컬럼값
                   , map_id=state) #지도에 표시할 컬럼값
             , map=states_map #지도 데이터, 위도 경도 값
             , interactive=T) #팝업창

######## 한국 지도
install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)
ds <- korpop1 #한국 인구 데이터
str(ds)

library(dplyr)
library(ggiraphExtra)
library(mapproj)
library(ggplot2)

# rename : 총인구_명 -> pop으로 변경, 행정구역별_읍면동 -> name으로 변경
ds <- rename(ds, pop=총인구_명, name=행정구역별_읍면동)
ds
str(kormap1) #위도경도
ggChoropleth(data=ds
             , aes(fill = pop
                   , map_id=code
                   , tooltip=name)
             , map=kormap1
             , interactive = T)

######### 시도별 결핵환자수를 지도에 표시
library(kormaps2014)
library(ggiraphExtra)
library(ggplot2)
tbc #NewPts = 결핵환자수

ggChoropleth(data=tbc
             , aes(fill = NewPts
                   , map_id=code
                   , tooltip=name)
             , map=kormap1
             , interactive = T)

########인터렉티브 그래프 구현
install.packages("plotly")
library(plotly)
library(ggplot2)
mpg
# displ 배기량
# hwy   고속 연비
# drv   구동방식. f(전륜구동), r(후륜구동), 4(4륜구동)
ggplot(data=mpg, aes(x=displ, y=hwy, col=drv))+geom_point()

p <- ggplot(data=mpg, aes(x=displ, y=hwy, col=drv))+geom_point()
ggplotly(p)

str(diamonds)
ggplot(data=diamonds, aes(x=cut, fill=clarity))+geom_bar(position = 'dodge')
p <- ggplot(data=diamonds, aes(x=cut, fill=clarity))+geom_bar(position = 'dodge')
ggplotly(p)
