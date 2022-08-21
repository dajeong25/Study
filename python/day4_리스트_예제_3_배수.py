#1차원 리스트 연습문제
#3) 1~100 사이의 정수 난수 10개 중에서 5의 배수의 개수, 합계, 평균 출력

import random

ran_number = []
ran_number_5 = []
count = 0
sum = 0

for i in range(10): 
    ran_number.append(random.randint(1, 100))
print("전체 리스트 : ", ran_number)

for j in ran_number:
    sum = j
    if j % 5 == 0:
        count += 1
        sum += sum
        ran_number_5.append(j)

if count == 0:
    print("전체 리스트 중 5의 배수가 없습니다.")

else :
    print("전체 리스트 중의 5의 배수 :", ran_number_5)
    print("리스트 내 5의 배수의 개수 :", count)
    print("리스트 내 5의 배수의 합계 :", sum)
    print("리스트 내 5의 배수의 평균 :", sum/count)


''' # 그 외 답안
import random
nums =[]
for i in range(0, 10) :
    nums.append(random.randint(1, 100))
print(nums)   

cnt =0
total = 0
for num in nums :
    if num %5 ==0 :
        cnt +=1
        total +=num

if cnt>0 :
    print("5의 배수 개수 :", cnt) 
    print("5의 배수 합계 :", total) 
    print("5의 배수 평균 :", total/cnt) 
else :
    print("5의 배수가 존재하지 않습니다")
'''

