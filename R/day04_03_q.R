### socsupport 데이이터셋 : 호주의 사회복지 서비스와 만족도 354p
library(DAAG)
str(socsupport)

# 1.연령별 비율을 3차원 원그래프로
library(plotrix)
tmp <- table(socsupport$age)
  # 18-20 21-24 25-30 31-40   40+ 
  #    44    35     6     6     4 
pie3D(tmp, main='연령별 비율', explode=0.05, labels=names(tmp), labelcex=1)

# 2. 정서적지원제도 분포를 호주|그 외 지역으로 나누어 상자그림으로
boxplot(emotional~country, data=socsupport, col=rainbow(2), main='정서적지원제도 비교')

# 3. 정서적지원제도 분포를 성별로 나눠 상자그림으로
boxplot(emotional~gender, data=socsupport, col=rainbow(2), main='정서적지원제도 성별 비교')

# 4. 정서적지원제도 분포를 연령대별로 나눠 상자그림으로
boxplot(emotional~age, data=socsupport, col=rainbow(5), main='정서적지원제도 연령대 비교')

# 5. 정서적지원제도&물질적 지원제도 만족도, 연령대를 성별에 따라 산점도로(모양, 색 달리)
target <- socsupport[, c('emotionalsat','tangiblesat', 'age')]
group <- as.numeric(socsupport$gender)
plot(target, main='성별에 따른 분포', pch=c(group), col=rainbow(length(levels(socsupport$gender))))
