# install.packages("wordcloud")
library(KoNLP) #Checking user defined dictionary! warning뜸
useNIADic() #디렉토리설정 
# useSejongDic() #디렉토리설정 안 해도 되는 듯?
library(wordcloud)
library(RColorBrewer)
# .libPaths() #해당 패스의 library 폴더에 KoNLP 압축파일 바로 넣기
############################### 실패
# install.packages("remotes") #외부파일을 패키지 설정을 위한 패키지
# remotes::install_github("haven-jeon/KoNLP",
#                         upgrade = "never",
#                         INSTALL_opts = c("--no-multiarch"))
# install.packages("multilinguer")
# library(multilinguer)
# install_jdk()
# 
# install.packages(c("stringr", "hash", "tau", "Sejong", "RSQLite", "devtools"),
#                  type = "binary")
# 
# install.packages("cli") #이것까진 안 해도 되는 듯
######################## 성공!
# buildDictionary(ext_dic='woorimalsam') # "우리말씀" 한글 사전 로딩 : 안 해도 됨
setwd("d:/emspy/R/data")

# readLines 한 줄씩 읽어 옴
text <- readLines("mis_document.txt", encoding='utf-8') # 비정형 한글 문서
text
# apply : 벡터에서 함수 적용 함수
# sapply(문자열, 함수명, 옵션) : 문자열에서 함수 적용하여 추출
noun <- sapply(text, extractNoun, USE.NAMES = F) #text 데이터에서 명사 추출. 헤더 없음
noun
noun2 <- unlist(noun) #추출된 명사 통합
noun2
wordcount <- table(noun2) #단어 빈도수
wordcount

#단어 빈도수가 높은 순으로 정렬
temp <- sort(wordcount, decreasing=T)[2:10] #공백제외
temp 
barplot(temp, names.arg=names(temp), col = "lightblue"
        , main="빈도수 높은 단어", ylab="단어빈도수")
pal2 <- brewer.pal(8, "Dark2")
wordcloud(names(wordcount) #출력할 단어들
          , freq=wordcount #단어들의 빈도수
          , scale=c(6,0.7) #폰트크기
          , min.freq=5     #최소 빈도수
          , random.order=F #출력 위치
          , rot.per=.1     #90도 회전 단어 비율
          , colors=pal2)   #단어들의 색상 설정

# 1. 글자 1개인 단어 제거
length(noun2) # 1075 단어개수
noun2 <- noun2[nchar(noun2) > 1]
length(noun2) #825 : 1글자 제거
# 2. 의미없는 단어 제거 gsub == replace
noun2 <-gsub("들이","", noun2)
noun2 <-gsub("첫째","", noun2)
noun2 <- noun2[nchar(noun2) > 1] #이걸 안 하면 빈문자열로 자리 남아있음(개수변동x)
length(noun2) #819
# 3. 숫자들 제거. 정규식 패턴 사용
noun2 <- gsub("[0-9]",'', noun2)
noun2 <- noun2[nchar(noun2) > 1]
length(noun2) #814
wordcount <- table(noun2)
wordcount
temp <- sort(wordcount, decreasing = T)
temp
wordcloud(names(wordcount) #출력할 단어들
          , freq=wordcount #단어들의 빈도수
          , scale=c(6,0.7) #폰트크기
          , min.freq=5     #최소 빈도수
          , random.order=F #출력 위치
          , rot.per=.1     #90도 회전 단어 비율
          , colors=pal2)   #단어들의 색상 설정

wordcloud(c(letters, LETTERS, 0:9), seq(1,1000, len=62), colors=palete)
# letters 소문자 / LETTERS 대문자
# c(letters, LETTERS, 0:9) : 26+26+10 => 62가지 문자
# seq(1,1000, len=62) : 1~1000의 숫자를 62개로 나누어
seq(1,1000, len=62)
LETTERS

# library(RColorBrewer) wordcloud 설치하면 자동으로 함께 설치함
palete <- brewer.pal(9, "Set1") #색상표
palete
wordcloud(c(letters, LETTERS, 0:9), seq(1,1000, len=62), colors=palete)

