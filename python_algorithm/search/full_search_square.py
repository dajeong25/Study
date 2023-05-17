# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 완전탐색 - 제곱암호
import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
answer = ''
for i in range(1,N+1, 2):
	string = s[i-1]
	num = int(s[i])
	answer += chr( (ord(string) - ord('a') + num**2) % 26 + ord('a') )

print(answer)

# if문으로 나누면서 예상치못한 케이스들이 생겨서 fail
# if/else로 나눈 것을 한번에 계산하면 오히려 문제가 안 생김.

# !!먼저 if문을 하기 보단 계산해서 한번에 계산할 생각하기!!