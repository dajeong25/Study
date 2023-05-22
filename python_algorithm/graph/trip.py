# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그래프 탐색 - 구름이의 여행1
# [다시] 처음 작성 시 에러나서 해설 참고한 것


import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 섬개수, 다리개수, 구름이 건널 최대 다리개수
N, M, K = map(int, input().split())

route = defaultdict(list)
for i in range(M):
	start, end = map(int, input().split())
	route[start].append(end)
	route[end].append(start)

q = deque()
q.append(1)
visited = [10e9 for _ in range(N+1)]
visited[1] = 0

while q:
	node = q.popleft()
	for next_node in route[node]:
		if visited[next_node] <= visited[node] +1:
			continue
		visited[next_node] = visited[node]+1
		q.append(next_node)
	
if visited[N] <= K:
	print("YES")
else:
	print("NO")
