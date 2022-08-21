'''
set을 사용하여 로또 번호 추첨처럼 1~45의 숫자 중에서 
중복 없이 6개를 뽑는 프로그램을 구현하시오
[Sample Run] 
** 로또 추첨을 시작합니다. **
추첨된 로또 번호 --> 2, 6, 8, 27, 32, 41
'''
import random

lotto_set = set()
while len(lotto_set) < 6: 
    lotto_set.add(random.randint(1, 45))

lotto = list(lotto_set) 
lotto.sort()
print("** 로또 추첨을 시작합니다. **")
print("추첨된 로또 번호 ->", end=" ")
for i in lotto:
    print(i, end=" ")


''' # 그 외 답안
import random
print("** 로또 추첨을 시작합니다. **")
lotto = set()
for i in range(6) :
    lotto.add(random.randrange(1,45))
print("추첨된 로또 번호 --->",lotto)

#답안2
import random
lotto=set()
while True:
    n=random.randint(1,45)
    lotto.add(n)
    if len(lotto)==6:
        print("로또 당첨 번호는",lotto," 입니다.")
        break
    else:
        continue
'''


