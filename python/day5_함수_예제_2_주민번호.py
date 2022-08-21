'''
Q5>주민번호를 입력하면 유효한지 유효하지 않은지 
bool값으로 반환하는 함수를 정의하고 함수를 실행시켜서 결과를 출력하시오

[사용자로부터 주민번호 입력 받음] 000000-0000000 (문자열로 읽어들임)
-을 제외시키고 한문자 한문자를 정수로 변환해서 int[] 에 저장 (배열의 크기는 13)

[주민번호 체크]
주민번호 앞에서부터 12자리의 각 자리의 수에 가중치 { 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5 }를 곱합니다.
곱한수를 모두 더하여 총합을 구하고, 그 총합을 11로 나눈 나머지를 구합니다.
그 나머지를 11에서 뺀 결과가 CHECK DIGIT 입니다.
뺀 결과가 2자리수인 경우에는 2자리수를 10으로 나눈 나머지가 CHECK DIGIT가 됩니다.
CHECK DIGIT의 값이 입력 숫자 스트링의 13번째 숫자와 같으면 "CORRECT", 다르면 "INCORRECT"를 출력합니다.
'''
def input_jumin():
    print('주민번호 유효성 체크하는 프로그램입니다.')
    print('입력예시 : 123456-1234567')
    jumin = input('주민번호 입력 : ')
    jumin_nums = []
    for i in jumin:
        if '-' == i:
            continue
        else:
            jumin_nums.append(int(i))
    return check_jumin(jumin_nums)

def check_jumin(jumin_nums): #주민번호 체크
    digit = 2
    total = 0
    for idx in jumin_nums:
        if digit == 10: #가중치 ~2, 3, 4, 5 }
            digit = 2
        total += jumin_nums[idx]*digit #곱한수를 모두 더하여 총합을 구합니다.
        digit += 1 #{ 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5 }를 곱합니다.
    check_digit = (11 - total%11)%10
    if check_digit == jumin_nums[12]:
        print("CORRECT")
    else:
        print("INCORRECT")

input_jumin()

''' # 그 외 답안
#주민번호 입력받아서 인수로 전달
def check_jumin(jumin_number):
    pass
#호출된 함수 내부에서 주민번호 입력받아서 체크
def chech_jumin():
    jumin_str = input("주민번호 입력(000000-0000000): ")
    jumin_nums = []

    for s in jumin_str:
        if s == "-":
            continue
        else:
            jumin_nums.append(int(s))
    
    digit = 2
    total = 0
    for idx in range(len(jumin_nums)-1):
        if digit == 10:
            digit = 2
        total += jumin_nums[idx]*digit
        digit += 1
    
    check_digit = (11 - total%11) % 10
    if (check_digit == jumin_nums[-1]):
        print("CORRECT")
    else:
        print("INCORRECT")

chech_jumin()'''