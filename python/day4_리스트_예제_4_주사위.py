'''1차원 리스트 연습문제
4) 주사위를 10번 던져서 각 숫자가 몇 번씩 나왔는지 알아보려 한다.
리스트를 활용하여 리스트에 각 주사위를 던져 나온 숫자의 개수를 저장하고 출력하시오'''

import random
dice = []
for i in range(10): 
    dice.append(random.randint(1, 6))

print("1이 나온 개수 :", dice.count(1))
print("2이 나온 개수 :", dice.count(2))
print("3이 나온 개수 :", dice.count(3))
print("4이 나온 개수 :", dice.count(4))
print("5이 나온 개수 :", dice.count(5))
print("6이 나온 개수 :", dice.count(6))


'''# 그 외 답안
import random
list_dice = [] #주사위값 저장
list_count = []  #주사위 1~6 나온 회수

for i in range(0, 10) :
    list_dice.append(random.randint(1, 6))
    
for j in range(1, 7):   #6번 반복
    list_count.append(list_dice.count(j))
    print(j, "이 나온 횟수는", list_dice.count(j) ,"번입니다.")


#답안2
import random

x = [] 
for i in range(10):
    a = random.randrange(1,7) 
    x.append(a)

for j in range(1,7):
    b = x.count(j)
    print(j,"는 ",b,"번 나왔습니다.")


#답안3
random.seed('0804')
lst = [random.randrange(1,7) for i in range(10)]
['주사위 '+str(i)+'의 눈 '+str(lst.count(i))+'번' for i in range(1,7)]


#답안4
import random as rd
dice = []
count = []
for i in range(10):
    dice.append(rd.randrange(1,7))   # 주사위 10번 굴리기

dice.sort() # 주사위 수 정렬
print("주사위 :",dice) # 주사위 수 확인

print("바뀌는 지점 : ", end = " ") # 주사위 수 비교
for i in range(1,10):
    if dice[i-1] != dice[i]:
        count.append(i)
        print(count.pop(),end = " ")
        count.append(i)
print()
for i in range(int(len(count))):    
    if i == 0:
        print(dice[count[i]-1], count[i],sep = ":",end = "개 \n")
    else:
        print(dice[count[i]-1], count[i]-count[i-1],sep = ":",end = "개 \n")
print(dice[count[i]],10-count[i],sep = ":",end = "개 \n")


#답안5
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for i in range(10):
    k = random.randint(1, 6)
    if k == 1:
        num1 += 1
    if k == 2:
        num2 += 1
    if k == 3:
        num3 += 1
    if k == 4:
        num4 += 1
    if k == 5:
        num5 += 1
    if k == 6:
        num6 += 1
        
print("1은", num1, "개","2은", num2, "개","3은", num3, "개","4은", num4, "개","5은", num5, "개","6은", num6, "개")


#답안6
import random

dice_count=[0, 0, 0, 0, 0, 0]
for i in range(0, 10) : 
    dice = random.randint(1, 6)
    dice_count[dice-1] +=1
    print(dice, end=" ")
print( )

for cnt in range(0, 6) : #0,1,2,3,4,5
    print("dice number ", cnt+1 ,"의 개수는 ",  dice_count[cnt])
'''
