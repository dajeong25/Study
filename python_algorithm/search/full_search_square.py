# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 완전탐색 - 제곱암호
import sys
input = sys.stdin.readline

N = int(input())
s = input()
answer = ''
string = ''
num = 0
for i in range(1,N+1, 2):
	string = s[i-1]
	num = int(s[i])
	idx = ord(string) - ord('a') + 1
	if (idx+(num**2)) > 26:
		answer += chr((idx+(num**2))%26-1 + 97)
	else:
		answer += chr(ord(string)+num**2)

print(answer)