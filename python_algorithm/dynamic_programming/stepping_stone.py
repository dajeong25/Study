# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 다이나믹 프로그래밍 - 조건 있는 징검다리 건너기 (사후)
# [다시] 한번에 3칸, 최소 독극물
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
po = list(map(int, input().split())) + [0]

# 세칸의 최소계산 > 한칸이동 세칸의 최소 비용 계산 
if N < 3:
	print(0)
else:
	q = deque()
	q.append(po[0])
	q.append(po[1])
	q.append(po[2])
	# print(q)

	for i in range(3, N+1):
		plus = min(q) + po[i]
		q.append(plus)
		q.popleft()
		# print(q)

	print(q[-1])