#4. 나르시스트의 수 구하기_힌트:%연산자 활용(모듈러) 3자리의 양의 정수만 실행합니다.
#100의 자릿수, 10의 자릿수, 1의 자릿수를 각각 구하고, 
#각 자릿수를 3제곱하여 더한 수와 원래의 수와 같은지를 비교하여 같은 수를 출력하시오
#마지막에 이러한 수들의 총 개수를 구하시오(4개)

narcissist = 0
num_hun = 0 
num_ten = 0
num_one = 0
num_cal = 0

for num in range(100, 1000):
    num_hun = num // 100        #백의 자리수
    num_ten = (num % 100) // 10 #십의 자리수
    num_one = num % 10          #일의  자리수
    num_cal = num_hun**3 + num_ten**3 + num_one**3

    if num == num_cal :
        print("나르시스트 수 :", num_cal)
        narcissist += 1

print("나르시스트의 수의 총 개수 :", narcissist)


'''
cnt = 0  #나르시스트 수 개수 저장할 변수
num_list = range(100, 1000, 1)
print("100~999 사이의 나르시스트의 수는 ",   end= " ")
for i in num_list:              #for i in range(100, 1000, 1):  
    x = int(i / 100)            #백의 자리수
    y = int((i%100) / 10)     #십의 자리수
    z = i % 10                 #일의  자리수

    target = x**3 + y**3 + z**3

    if i == target:
        print(i , end =", ")
        cnt += 1
print()
print("나르시스트의 수 개수는 %d 개 입니다." % cnt)

'''