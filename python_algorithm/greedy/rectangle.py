# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# [다시] 그리디 알고리즘, 원인과 결과 찾기 - 직사각형 만들기
'''
N개의 막대기 중 일부 사용해서,
최대한 많은 직사각형을 만들면서 직사각형들의 넓이 합이 최대값
- 1차시도
    : 전체 쌍을 확인 후, 쌍의 개수가 홀수면 쌍 중에서 가장 작은수 하나를 빼고 계산
    : 반만 pass
    : 생각해보니까 쌍을 찾는 과정에서 에러난 듯
- 2차시도
    : 홀수가 문제이기 때문에 개수를 세고 몫만 추가하는 것으로 했지만 런타임 에러...
    : deque로 추가하고 pop으로 빼는 것 자체가 시간 초과..
- 3차시도 : pop이랑 if문을 빼고 순서를 그대로 했는데도 시간 초과..ㅠ
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
S = list(map(int, input().split()))

co = []
if N <= 1:
	print(0)
else:
	cnt = [0 for _ in range(10**6)]
	for s in S:
		cnt[s] += 1
		
	for i in range(10**6):
		if cnt[i] > 1:
			for _ in range(cnt[i]//2):
				co.append(i)
	# print(1, co)
	
	co.sort(reverse=True)
	area = 0
	for i in range(1, len(co), 2):
		area += co[i-1] * co[i]
	print(area)


#해설
import sys
input = sys.stdin.readline

N = int(input())
pair = []
cnt = [0 for _ in range(1000001)]
sticks = map(int, input().split())
for stick in sticks:
    cnt[stick] += 1

for length in range(1, 1000001):
    while cnt[length] > 1:
        cnt[length] -= 2
        pair.append(length)

pair.sort(reverse=True)
ans = 0
for i in range(1, len(pair), 2):
    ans += pair[i - 1] * pair[i]

print(ans)