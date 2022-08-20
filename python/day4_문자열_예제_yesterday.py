f = open('yesterday.txt', 'r')
content = f.read()
words = content.split() #단어 토큰화, 리스트로 리턴
count = 0
for word in words :
    if word.upper().strip() == 'YESTERDAY' :
        count+=1

print("Number of word 'Yesterday' : " , count)


#count함수 사용
f = open("Yesterday.txt", "r").read() #여기서는 파일을 닫으려면 연 파일을 변수로 따로 받아야함.
content = f.lower()
print("Number of a Word 'Yesterday'", content.count("yesterday"))
