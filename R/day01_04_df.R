# dataFrame

## dataframe 객체 생성
# 1. 벡터를 이용한 생성
no <- c(1,2,3,4)
name <- c('Apple','Peach','Banana','Grape')
price = c(500,1000,500,2000)
qty <- c(5,2,6,1)

#dataframe 생성
sales <- data.frame(NO=no, NAME=name, Price=price, QTY=qty)
sales
  #   NO   NAME Price QTY
  # 1  1  Apple   500   5
  # 2  2  Peach  1000   2
  # 3  3 Banana   500   6
  # 4  4  Grape  2000   1

# 조회
sales[1,3] #500 1행 3열
sales[1,]  #1행 조회
sales[1]   #1열 조회
sales[c(1,3),] #1행,3행 조회
sales[c(1,3)]  #1열, 3열 조회
sales[,c(1,3)]  #1열, 3열 조회
sales[c(1,3), c(1,3)] #1행, 3행 중 1열과 3열만 데이터만 출력
sales[1:3,] #1~3행 출력
sales[1:3, 2:4] #1~3행 중 2~4열 데이터만 출력


x <- c(1,'Apple',500,5,2,'Peach',1000,2,3,'Banana',500,6,4,'Grape','2000',1)
m1 <- matrix(x, nrow=4, byrow=T)
m1
  #     [,1] [,2]     [,3]   [,4]
  # [1,] "1"  "Apple"  "500"  "5" 
  # [2,] "2"  "Peach"  "1000" "2" 
  # [3,] "3"  "Banana" "500"  "6" 
  # [4,] "4"  "Grape"  "2000" "1"

# matrix를 dataframe으로
sales2 = data.frame(m1)
sales2
  # X1     X2   X3 X4
  # 1  1  Apple  500  5
  # 2  2  Peach 1000  2
  # 3  3 Banana  500  6
  # 4  4  Grape 2000  1
names(sales2) = c('NO', "NAME", 'Price', 'QTY')
sales2
mode(sales2) #"list"
length(sales2) #4
length(m1) #16

#열이름 조회
names(sales2)
#행이름 조회
row.names(sales2)
row.names(sales2) <- c('A','B','C','D')

# 수량이 5개 미만인 상품 검색
# subset() : 조건으로 검색
subset(sales2, QTY < 5)
# 가격이 2000인 데이터 조회
subset(sales2, Price==2000)

# 벡터데이터 조건
x = 1:10
x
#10이상인 데이터 조회
x[x>=5] # TRUE인 값만 출력
x>=5    # TRUE / FALSE로 출력

#x 데이터 중 짝수인 데이터만 출력
x[x%%2==0]

no <- c(1,2,3)
name <- c('apple', 'banana','peach')
price <- c(100,200,300)
df1 <- data.frame(no, name, price)
df1

no <- c(10,20,30)
name <- c('train', 'car','airplain')
price <- c(1000,2000,3000)
df2 <- data.frame(no, name, price)
df2

df3 <- rbind(df1, df2)
df3
df4 <- cbind(df1, df2)
df4


x <- data.frame(matrix(1:9, 3))
names(x) <- c('c1', 'c2', 'c3')
row.names(x) <- c('r1','r2','r3')
x

#or
m <- matrix(1:9, 3, dimnames=list(c('r1','r2','r3'), c('c1', 'c2', 'c3')))
m
x <- data.frame(m)
x



#행의 개수와 열의 개수 구하기
length(x)

nrow(x)
ncol(x)



# 문제1
x = c(2,-1,3,7,0.5,8)
x
# 1. 6,2,4번째 원소를 동시에 찾아라
x1 <- matrix(x)
x1[c(6,2,4)] #8 1 7

# 2. x의 원소 중 0보다 큰 값을 찾아라
x[x>0] #2.0 3.0 7.0 0.5 8.0

# 3. 짝수 원소 찾아라
x[x%%2==0] #2 8

# 4. x에서 홀수원소를 찾아 제거하고 결측값을 생성하라
x[x%%2==1] <- NA
x #2.0  NA  NA  NA 0.5 8.0

# 5. x에서 홀수원소를 찾아 제거하고 결측값 없음
setdiff(x, x[x%%2==1]) #2.0 0.5 8.0


# 문제2
L = list(ID=c(1,2,3,4)
         , name=c('Kim','Lee','Park','E')
         , score=c(80,95,75, 20))

# 1. length(L)은 얼마이며, 이것은 무엇을 의미하는가
length(L) #3 : 속성 값의 개수 출력(컬럼) >> 테이터 종류의 개수(key 값)

# 2. 성적 75를 80으로 수정하라
L$score[L$score==75] <- 80
L$score

# 3. L$name=='Park'의 결과를 쓰고 무엇을 의미하는지 설명하라
L$name=='Park' # FALSE FALSE  TRUE : name의 값 중에 Park과 일치하면 T, 일치하지 않으면 F

# 4. L$score[L$name=="Park"]의 결과를 쓰고, 무엇을 의미하는지 설명하라
L$score[L$name=="Park"] #80 : name이 Park인 사람의 점수 값을 출력해줌

# 5. 1번 학생의 이름과 성적을 조회하라
L <- data.frame(L)
L[1, 2:3]
  #   name score
  # 1  Kim    80
ncol(L)
length(L)
nrow(L)
length(df4)
ncol(df4)
nrow(df4)
