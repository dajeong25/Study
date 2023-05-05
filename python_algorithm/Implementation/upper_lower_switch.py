'''
출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반

대소문자 바꾸기
'''
n = int(input())
words = input()
capital = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]

answer = ''
for word in words:
	if word in capital:
		answer += word.lower()
	else:
		answer += word.upper()
print(answer)

# 파이썬은 입력 받은 문자열을 문자 단위로 읽어서 변환하기 때문에 느림
# >> 입력이 많을 때는 sys 활용! 
# >> 단, 개행문자(\n)을 포함하여 저장되기때문에 공백제거하면 좋음
import sys
n = int(sys.stdin.readline().rstrip())
words = sys.stdin.readline().rstrip()

# 1. 파이썬에는 islower(), isupper() 메소드가 있음.....wow...
answer = ''
for word in words:
	if word.isupper():
		answer += word.lower()
	else:
		answer += word.upper()
print(answer)

# 2. swapcase() 메소드를 한번에 해결 가능..!
print(words.swapcase())
