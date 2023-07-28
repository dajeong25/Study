## R에서 제공하는 iris 데이터 분석 ##

head(iris) #처음 6개 데이터 조회
tail(iris) #마지막 6개 데이터 조회
class(iris)#"data.frame" : iris 데이터 자료형
dim(iris)  #150 5 : 행과 열의 개수
nrow(iris) #150 : 행의 개수
ncol(iris) #5   : 열의 개수
colnames(iris) #열의 이름 "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species"

# iris 데이터의 요약정보
str(iris)

#Species 컬럼만 조회
iris[, 'Species']
iris[, 5]

# iris 데이터의 Species 컬럼 levels 조회
levels(iris[,5]) #"setosa" "versicolor" "virginica" 

# 품종별 데이터 개수 조회하기
table(iris[,5])
  # setosa versicolor  virginica 
  #     50         50         50 

str(iris)
iris[,-5]
iris
## data.frame 형식 유지해야함
# 열별 합계 조회
colSums(iris[,-5])
# 열별 평균 조회
colMeans(iris[,-5])
# 행별 합계 조회
rowSums(iris[, -5])
# 행별 평균 조회
rowMeans(iris[, -5])

#조건에 맞는 행들만 조회
iris1 <- subset(iris, Species=='setosa')
str(iris1)
levels(iris1[,5]) #"setosa" "versicolor" "virginica" : 원본 데이터를 함께 보여줌

#Sepal.Length >5 크고, Sepal.width >4 보다 큰 행들만 iris2 데이터 저장하기
iris2 <- subset(iris, Sepal.Length>5 & Sepal.Width>4)
str(iris2)
  #   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
  # 16          5.7         4.4          1.5         0.4  setosa
  # 33          5.2         4.1          1.5         0.1  setosa
  # 34          5.5         4.2          1.4         0.2  setosa

#컬럼 조회하기
#Sepal.Length >5 크고, Sepal.width >4 보다 큰 행들의 Petal.Length, Petal.Width, Species 컬럼만 조회
iris2 <- subset(iris, Sepal.Length>5 & Sepal.Width>4)
iris2[, 3:5]

subset(iris, Sepal.Length > 5 & Sepal.Width >4)[,3:5]
subset(iris, Sepal.Length > 5 & Sepal.Width >4)[,c(3,4,5)]

class(iris) #"data.frame"

## 미국 주의 정보 데이터
class(state.x77) #"matrix" "array"
state.x77

#조건 함수 : 결과 TRUE, FALSE
is.matrix(iris)      #FALSE : "data.frame" DATA
is.matrix(state.x77) #TRUE  : "matrix" "array" DATA
is.data.frame(iris)  #TRUE
is.data.frame(state.x77) #FALSE

## matrix -> data.frame
df77 <- data.frame(state.x77)
class(df77)
str(df77)
str(state.x77)

## data.frame => matrix : 전체 문자열로 바뀜 why? 자료형이 동일해야함.
miris <- as.matrix(iris)
miris
miris <- as.matrix(iris[, -5])
miris
class(miris) #"matrix" "array" 


## trees 데이터 : 벚나무의 정보를 저장한 데이터
# 1. 직경 Girth의 평균값 구하기
str(trees)
colMeans(trees[1])
mean(trees[, 1])
mean(trees$Girth)
mean(trees[, 'Girth'])

# 2. 직경 Girth이 전체 직경 평균값 보다 큰 데이터만 조회
subset(trees, Girth > colMeans(trees[1]))
subset(trees, Girth > mean(trees$Girth))

# 3. 직경 Girth > 전체 평균 / 높이 Height > 80 / 부피 Volume > 50
  #  selltree에 저장하고 레코드 개수 출력
selltree <- subset(trees, Girth>colMeans(trees[1])&Height>80&Volume>50)
selltree <- subset(trees, Girth>colMeans(trees["Girth"])&Height>80&Volume>50)
selltree <- subset(trees, Girth>mean(trees$Girth)&Height>80&Volume>50)
selltree <- subset(trees, Girth>mean(trees[,1])&Height>80&Volume>50)
print(selltree)
print(nrow(selltree))


####
# 1. R에서 제공하는 cars 데이터셋은 자동차와 속도와 제동거리에 대한 자료이다.
#   이 데이터셋에 대해 다음 문제를 해결하기 위한 코드 작성
# (1) 이 데이터셋의 자료구조는?
class(cars) #"data.frame"

# (2) 이 데이터셋의 관측값(행)과 컬럼(변수)의 개수는?
cat(nrow(cars), ncol(cars)) # 50 2
# or
dim(cars) #50  2

# (3) 이 데이터셋의 앞쪽 일부분의 내용을 보이시오
print(head(cars))
print(head(cars,4))

# (4) 이 데이터셋의 요약 정보를 조회
str(cars)

# (5) 이 데이터셋의 컬럼별 평균은?
print(colMeans(cars))
  # speed  dist 
  # 15.40 42.98 

# (6) 가장 긴 제동거리 dist는?
print(max(cars$dist)) #120

# (7) 제동거리가 가장 길 때의 속력 speed와 제동거리dist는?
print(subset(cars, dist==max(cars$dist)))
  #    speed dist
  # 49    24  120

# 2. R에서 제공하는 InsectSprays 데이터셋은 살충제의 효과를 실험한 자료이다.
#   이 데이터셋에 대한 다음 문제를 해결하기 위한 코드를 작성하시오
# (1) 이 데이터셋의 자료구조가 매트릭스 인가?
print(is.matrix(InsectSprays)) #FALSE

# (2) 이 데이터셋의 요약 정보를 조회
str(InsectSprays)

# (3) 이 데이터셋의 뒤쪽 10개의 내용 조회
print(tail(InsectSprays, n=10))

# (4) 실험에 사용한 살충제 spray의 종류는?
print(levels(InsectSprays$spray)) #"A" "B" "C" "D" "E" "F"

# (5) 살충제별 데이터의 빈도는?
for (i in c(levels(InsectSprays$spray))){
  s <- subset(InsectSprays, spray == i)
  cat(i, nrow(s[1]), "\n")
  }
      # A 12 
      # B 12 
      # C 12 
      # D 12 
      # E 12 
      # F 12
# or
print(table(InsectSprays$spray))
  # A  B  C  D  E  F 
  # 12 12 12 12 12 12 

# (6) 살충제 E의 자료만 추출하여 InsectSprays.e에 저장하시오
InsectSprays.e <- subset(InsectSprays, spray == "E")

# (7) 살충제 E가 박명한 해충수 count의 평균은?
mean(InsectSprays.e[, 1]) #3.5
