#1~100사이의 정수 난수 10개 중에서 max값 출력
#(np.max함수와 같이 이미 만들어져 있는 함수 사용하지 말것)

import random

ran_number = []
for i in range(10): 
    ran_number.append(random.randint(1, 100))

ran_number.sort()
print("저장된 난수 10개 :", ran_number)
print("난수 중에서 가장 큰 값 :", ran_number[9])


''' # 그 외 답안
#방법1
import random
nums =[]
for i in range(0, 10) :
    nums.append(random.randint(1, 100)) 
print(nums)   
max = nums[0]
for i in range(1, 10) :
    if (max<nums[i]) :
        max = nums[i]
print(max) 


##방법2
import random
nums = []
text=0
for i in range(10) :
    nums.append(random.randrange(1,101)) 
nums.sort()
print(nums[9])


###방법3
import random
num=[] 
for i in range(10):
    num.append(random.randint(1,100))
print(num)

print(max(num))
'''
