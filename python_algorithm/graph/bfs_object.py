# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그래프 탐색 - 물체 탐색 (사후)
# 1차시도 - 3개 통과되고 실패.
# 2차시도 - max 값이 무한히 늘어나는 코드를 수정했지만 대다수 에러
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
obj = [input().strip() for _ in range(M)]

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
max_cnt = 1
visited = [[0 for _ in range(N)] for _ in range(M)]
for y in range(M):
	for x in range(N):
		if obj[y][x] == '#' and visited[y][x] != 1:
			visited[y][x] = 1
			cnt += 1
			temp_cnt = 1
			size = deque()
			size.append((y,x))
			while size:
				y, x = size.popleft()
				for i in range(4):
					ny = dy[i] + y
					nx = dx[i] + x
					if ny<0 or ny>=M or nx<0 or nx>=N :
						continue
					if obj[ny][nx] == '#' and visited[ny][nx] != 1:
						temp_cnt += 1
						size.append((ny,nx))
						visited[ny][nx] = 1
			if temp_cnt > max_cnt:
				max_cnt = temp_cnt
print(cnt)
print(max_cnt)
