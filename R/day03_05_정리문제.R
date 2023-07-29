# 1. mtcars 데이터셋에서 mpg, hp, wt 세 개의 열에 대한 각각의 평균을 구하려한다.
#   apply() 함수를 사용하여 코드 작성
apply(mtcars[,c('mpg','hp','wt')], 2,mean)
   #      mpg        hp        wt 
   # 20.09062 146.68750   3.21725 

# 2. USArrests 데이터셋은 1973년 미국 50개 주에서 발생한 강력 범죄에 대한 기록이다.
#   구체적으로 각 주를 관측값으로 하여 각 열에 대한 인구 10만명 당 살인Murder, 
#   폭행Assault, 강간Rape에 대한 체포건수를 저장하고 있다.
# 1) 살인 폭행 강간 범죄에 대한 체포건수의 합은 각각 얼마?
USArrests
colSums(USArrests[,-3])
   # Murder Assault    Rape 
   #  389.4  8538.0  1061.6 

# 2) 살인 폭행 강간 범죄에 대한 체포건수의 평균은 각각 얼마?
colMeans(USArrests[,-3])
   # Murder Assault    Rape 
   #  7.788 170.760  21.232

# 3) 살인 범죄 체포가 가장 많이 발생한 주는 어디?
row.names(USArrests[which.max(USArrests[,1]),]) # "Georgia"
row.names(USArrests)[which.max(USArrests[,1])]

# 4) 폭행 범죄 체포가 가장 적게 발생한 주의 살인 범죄 체포건수는?
USArrests[which.min(USArrests[,2]),1] # 0.8

# 3. sleep 데이터셋에 대한 컬럼 설명
# - extra : 수면 시간의 증가량
# - group : 사용한 약물의 종류
# - ID : 환자 식별 번호
str(sleep)
# 제목 : "수면증가량히스토그램", x축:증가량, y축:빈도수, 막대수4를
#  가진 히스토그램 작성
hist(sleep[,1], main="수면증가량히스토그램", xlab="증가량", ylab="빈도수", breaks=4)
