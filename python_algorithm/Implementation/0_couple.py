# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 소개팅해주기
import sys
input = sys.stdin.readline

n = int(input())
s_list = list(map(int, input().split()))
answer = 0
for s in s_list:
	if not -s in s_list:
		answer += s
print(answer) #timeout...

