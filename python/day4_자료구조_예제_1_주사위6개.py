'''
Q5> 같은 숫자가 나올 때까지 주사위 6개를 동시에 무한 반복해서 던진다.
같은 숫자가 나올 때까지 몇 번 던졌는지, 
1부터 6까지 연속된 숫자는 몇 번 나왔는지 출력하는 프로그램 코드를 작성하시오
[Sample Run] 
6개 주사위가 모두 동일한 숫자가 나옴> 2 2 2 2 2 2
6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수> 10652
6개가 동일한 숫자가 나올 때까지 1~6의 연속번호가 나온 횟수> 172 
'''
import random

count = 0
count_set = 0
while True:
    dice = set()
    for _ in range(6): 
        dice.add(random.randint(1, 6))
    count += 1 #주사위를 던진 횟수 1증가
    
    if len(dice) == 1:
        break
    elif len(dice) == 6:
        count_set += 1
        continue
    else:
        continue

print(f"6개 주사위가 모두 동일한 {dice}이(가) 나옴")
print("주사위를 던진 횟수:", count)
print("1~6의 연속번호가 나온 횟수:", count_set)


''' #그 외 답안
import random
count = 0    #주사위를 던진 횟수
all_count = 0   #주사위값이 1, 2, 3, 4,5, 6이면 연속번호가 나온 횟수

while True:
    x = []   #주사위 6개 숫자 생성해서 list 에 저장
    count += 1 
    for i in range(6):
        a = random.randint(1,6)
        x.append(a)
        
    if len(set(x)) == 6:   #list객체를 set으로 변환
        all_count += 1
        continue
        
    elif len(set(x)) == 1:
        break
        
    else:
        continue

print("총",count,"번 굴리셨습니다.")
print("연속된 숫자는 총",all_count,"번 나왔습니다.")
'''
