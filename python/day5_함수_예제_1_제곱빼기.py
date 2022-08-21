'''
Q4> 함수로 만들고 호출해서 결과 출력
두 개의 음이 아닌 정수를 입력받아 큰 수의 제곱에서 작은 수의 제곱을 뺀 결과값을 
반환하는 함수를 정의하고 print(함수이름(8, 10)) 실행시키시오
'''

def square_subtraction(num1, num2):
    num1 = int(input('음이 아닌 정수1 : '))
    num2 = int(input('음이 아닌 정수2 : '))
    return abs(num1**2 - num2**2)

print(square_subtraction(8, 10))
