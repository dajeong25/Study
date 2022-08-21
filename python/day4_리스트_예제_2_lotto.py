#1차원 리스트 연습문제
#lotto 번호 생성해서 리스트에 저장하고 출력
#(로또 번호는 1~45의 숫자 중 6개의 중복값 없음. 출력은 오름차순, set객체 금지)

import random

lotto = []
number = 0

while len(lotto) < 6: 
    number = random.randint(1, 45)
    if not number in lotto:
        lotto.append(number)

lotto.sort()
print('** 로또 추첨을 시작합니다. **')
print('추첨된 로또 번호 >', lotto)

''' # 그 외 답안
import random
lotto=[]
while len(lotto) < 6:
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

print("pick list : ",end=""); print(lotto)
lotto.sort()
print("pick list : ",end=""); print(lotto)
lotto.sort(reverse=True)
print("pick list : ",end=""); print(lotto)

#sorted(list 객체)는 내장 함수 > 데이터 요소를 정렬한 새로운 list객체 리턴
#sort()는 리스트의 메서드 = None리턴, 리스트에 저장된 데이터 요소를 정렬
#       > 내림차순 정렬 : reverse=True

'''


