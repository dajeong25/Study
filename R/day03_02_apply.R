### apply 함수
# apply( DATA, row(1)|col(2), 적용함수 )
str(iris)

#iris 데이터에서 꽃받침, 꽃잎의 가로, 세로의 평균 출력하기
colMeans(iris[1:4])
  # Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
  #     5.843333     3.057333     3.758000     1.199333 
rowMeans(iris[,1:4])
  # [1] 2.550 2.375 2.350 2.350 


# iris[,1:4] : 모든 행, 1~4번째 컬럼까지의 데이터
apply(iris[,1:4], 2, mean) #열별 평균
  # Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
  #     5.843333     3.057333     3.758000     1.199333 
apply(iris[,1:4], 1, mean) #행별 평균
  # [1] 2.550 2.375 2.350 2.350


### 응시자 10명의 점수
s1 <- c(14,16,12,20,8,6,12,18,16,10)
s2 <- c(18,14,14,16,10,12,10,20,14,14)
s3 <- c(44,38,30,48,42,50,36,52,54,32)
score <- data.frame(s1, s2, s3)
score

#응시자별 과목 총첨 출력
total <- rowSums(score) 
total <- apply(score, 1, sum)
  #76 68 56 84 60 68 58 90 84 56

# total 데이터를 열로 추가하여 scoreset 데이터에 저장
scoreset <- cbind(score, total)
scoreset
  #    s1 s2 s3 total
  # 1  14 18 44    76
  # 2  16 14 38    68
  # 3  12 14 30    56
  # 4  20 16 48    84
  # 5   8 10 42    60
  # 6   6 12 50    68
  # 7  12 10 36    58
  # 8  18 20 52    90
  # 9  16 14 54    84
  # 10 10 14 32    56

# Q.s1, s2 과목은 20점 만점, s3 과목은 60점 만점
#   각각 과목이 40% 이상 득점이 되고, 총합이 60점 이상인 경우 합격,
#   socreset 데이터에 합격, 불합격 여부 설정
result <- c()
for(i in 1:nrow(scoreset)){
  if(scoreset[i,1] < 20*0.4 | scoreset[i,2] < 20*0.4 | scoreset[i,3] < 20*0.6){
    result[i] <- "불합격"
  } else if (scoreset[i, 4] >= 60){
    result[i] <- "합격"
  } else{
    result[i] <- "불합격"
  }
}
result

#result 데이터를 socreset에 추가
socreset <- cbind(scoreset, result)
socreset
  # s1 s2 s3 total result
  # 1  14 18 44    76   합격
  # 2  16 14 38    68   합격
  # 3  12 14 30    56 불합격
  # 4  20 16 48    84   합격
  # 5   8 10 42    60   합격
  # 6   6 12 50    68 불합격
  # 7  12 10 36    58 불합격
  # 8  18 20 52    90   합격
  # 9  16 14 54    84   합격
  # 10 10 14 32    56 불합격

## 위의 문제를 함수로 만들어서 apply로 적용해보기



