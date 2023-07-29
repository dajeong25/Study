### R교재 264p ###
# which(조건) : 조건에 맞는 데이터의 위치 리턴
# which.max(데이터) : 데이터 중 가장 큰 값의 위치 리턴
# which.min(데이터) : 데이터 중 가장 작은 값의 위치 리턴

score <- c(76,84,69,50,95,60,82,71,88,84)

#성적이 69인 학생은 몇번째?
which(score==69) #3
#84인 학생은?
which(score==84) #2 10
#85이상인 학생은?
which(score >= 85) #5 9

#성적이 가장 높은 학생은 어디?
max(score) #95
which.max(score) #5

#성적이 가장 낮은 학생은?
min(score) #50
which.min(score) #4

# 성적이 60점 이하인 학생의 점수를 61점으로 상향하자
score[which(score<=60)] <- 61 #76 84 69 61 95 61 82 71 88 84
score

# score 데이터에서 성적이 80이상인 점수를 조회
score[which(score>=80)]
subset(score, score>=80)
  # 84 95 82 88 84

score <- c(60,40,95,80)
names(score) <- c('John','Jane','Tom','David')
score 
   # John  Jane   Tom David 
   #   60    40    95    80 

#성적이 가장 좋은 사람의 이름 조회
names(score)[which.max(score)]
# Jane의 성적 조회
score[which(names(socre)=='Jane')]


#### 언어발달 상황 데이터 분석
install.packages('Stat2Data')
library(Stat2Data)
data() #사용할 수 있는 데이터 조회
data("ChildSpeaks") #ChildSpeaks 데이터 리턴
str(ChildSpeaks)
# Child : 번호
# Age : 말문 트인 시기
# Gesell : 언어 이해력 점수

# Age 컬럼이 9개월 미만이면 5등급 / 14미만이면 4등급 
#           / 20개월 미만이면 3등급 / 26개월 미만이면 2등급 / 그 이상은 1등급
idx <- which(ChildSpeaks$Age < 9)
idx
ChildSpeaks[idx, 'm1'] <- 5
ChildSpeaks
idx <- which(ChildSpeaks$Age >=9 & ChildSpeaks$Age < 14)
ChildSpeaks[idx, 'm1'] <- 4
idx <- which(ChildSpeaks$Age >=14 & ChildSpeaks$Age < 20)
ChildSpeaks[idx, 'm1'] <- 3
idx <- which(ChildSpeaks$Age >=20 & ChildSpeaks$Age < 26)
ChildSpeaks[idx, 'm1'] <- 2
idx <- which(ChildSpeaks$Age >=26)
ChildSpeaks[idx, 'm1'] <- 1
ChildSpeaks

# Gesell 컬럼
# 70미만 1등급 / 90미만 2등급 / 110미만 3등급 / 130미만이면 4등급 / 130이상이면 5등급
idx <- which(ChildSpeaks$Gesell < 70)
ChildSpeaks[idx, 'm2'] <- 1
idx <- which(ChildSpeaks$Gesell >= 70 & ChildSpeaks$Gesell < 90)
ChildSpeaks[idx, 'm2'] <- 2
idx <- which(ChildSpeaks$Gesell >= 90 & ChildSpeaks$Gesell < 110)
ChildSpeaks[idx, 'm2'] <- 3
idx <- which(ChildSpeaks$Gesell >= 110 & ChildSpeaks$Gesell < 130)
ChildSpeaks[idx, 'm2'] <- 4
idx <- which(ChildSpeaks$Gesell >= 130)
ChildSpeaks[idx, 'm2'] <- 5
ChildSpeaks

# total 컬럼 생성 : m1 + m2 의 합
ChildSpeaks$total <- ChildSpeaks$m1 + ChildSpeaks$m2
ChildSpeaks$total

# total 값
# 3미만 매우느림 / 5미만 느림 / 7미만 보통 / 9미만 빠름 / 이상 매우 빠름
idx <- which(ChildSpeaks$total < 3)
ChildSpeaks[idx, "result"] <- "매우느림"
idx <- which(ChildSpeaks$total >=3 & ChildSpeaks$total < 5)
ChildSpeaks[idx, "result"] <- "느림"
idx <- which(ChildSpeaks$total >=5 & ChildSpeaks$total < 7)
ChildSpeaks[idx, "result"] <- "보통"
idx <- which(ChildSpeaks$total >=7 & ChildSpeaks$total < 9)
ChildSpeaks[idx, "result"] <- "빠름"
idx <- which(ChildSpeaks$total >=9)
ChildSpeaks[idx, "result"] <- "매우빠름"
ChildSpeaks

# total 값이 가장 높은 아기의 정보 조회
ChildSpeaks[which.max(ChildSpeaks$total),]
  #    Child Age Gesell m1 m2 total   result
  # 11    11   7    113  5  4     9 매우빠름


