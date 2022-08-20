#6. 1~100사이의 소수 출력하기
prime_number = []
for num in range(2, 100):
    count = 0  #소수 개수 카운트

    for i in range(2,100):
        if num % i == 0: #나누어 떨어지면 i는 num의 약수
            count += 1
            if count >= 2: #나누어 떨어지는 수가 자기자신을 제외하고 
                break      #또 있다면 소수가 아님

    if count == 1:
        prime_number.append(num) #소수 리스트에 추가

print(prime_number)
print(f"소수의 총 개수는 {len(prime_number)}입니다.")


'''
flag = False
for i in range(2, 100) :
    if i == 2 or i ==3 or i==5 :
        flag = True
    else :
        for j in range (2, i) :     	
            if i%j ==0 :
                flag = False
                break
            else :
                flag = True
    if flag :
        print(i, end=" ")
'''

