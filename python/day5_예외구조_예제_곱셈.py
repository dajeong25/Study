'''
3) 세 개의 정수를 입력받아서 세 정수의 곱을 계산하고
계산한 결과에서 0~9의 숫자가 몇개씩 포함되어 있는지 출력하시오
[예시]				[출력 예시]
정수1 입력 : 150	150 x 266 x 427 = 17037300
정수2 입력 : 226	3 1 0 2 0 0 0 2 0 0
정수3 입력 : 427
'''
num = []
idx = 0
num_mul = 1
while idx < 3:
    try: 
        num.append(int(input(f'정수 {idx+1} 입력 : ')))
        num_mul *= num[idx]
        idx += 1
    except ValueError as e:
        print(e)

print(f'{num[0]} X {num[1]} X {num[2]} = {num_mul}')

num_mul = str(num_mul)
for i in range(10):
    print(f"{i}:{num_mul.count(str(i))}", end=" / ")
