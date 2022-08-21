'''
Q6> 입력된 문자열에서 숫자를 삭제하는 프로그램을 작성하시오
[Sample Run]  
문자열 -->  IT python 1234 Flask
숫자제거 -->  IT python  Flask 
'''

str_input = input("문자열을 입력해주세요 : ")
str_input = str_input.split(" ")

####### isdigit() 사용 #######
for value in str_input:
    if value.isdigit():
        str_input.remove(value)

####### try-except 구문 사용 #######
for value in str_input :
    try:
        if type(float(value)) == type(1.0):
            str_input.remove(value)
    except:
        continue

print("숫자를 제거한 문자열:", end=" ")
for i in str_input:
    print(i, end=" ")


'''#그 외 답안
txt = input()

for i in range(len(txt)):
    if txt[i].isdigit() == True :
        continue
    else :
        print(txt[i], end="")

text1=(input("문장을 입력하세요 : "))
text2 = ""
#print(dir(str))
for i in range(0,len(text1)) :
    if text1[i].isdigit() == False:
        text2 += text1[i]
print(text2)
'''
