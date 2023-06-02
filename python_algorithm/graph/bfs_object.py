# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그래프 탐색 - 물체 탐색 (사후)
# 1차시도 - 3개 통과되고 실패.
# 2차시도 - max 값이 무한히 늘어나는 코드를 수정했지만 대다수 에러
# 3차시도 - 멘토님께 여쭤봄 > 변수 설정의 에러였다..
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
p = [input().rstrip() for _ in range(M)]

# 상 하 좌 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

cnt = 0
max_size = 0
visited = [[0 for _ in range(N)] for _ in range(M)]
for y in range(M):
	for x in range(N):
		if p[y][x] == '#' and visited[y][x] == 0:
			visited[y][x] = 1
			cnt += 1
			temp = 0
			s = deque()
			s.append((y,x)) #여기의 y,x
			while s:
				sy, sx = s.popleft() #여기의 y,x가 동일하기 때문에 에러났음
				temp += 1
				for i in range(4):
					ny = dy[i] + sy
					nx = dx[i] + sx
					if ny<0 or ny>=M or nx<0 or nx>=N or p[ny][nx] == '.' or visited[ny][nx] == 1:
						continue
					s.append((ny,nx))
					visited[ny][nx] = 1
			max_size = max(temp, max_size)

print(cnt)
print(max_size)


#해설
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().rstrip() for _ in range(M)]
V = [[0 for _ in range(N)] for _ in range(M)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

component, ans = 0, 0
for i in range(M):
    for j in range(N):
        if V[i][j] or S[i][j] == '.':
            continue
        cnt = 0
        component += 1
        V[i][j] = 1
        Q = deque()
        Q.append((i, j))
        while Q:
            y, x = Q.popleft()
            cnt += 1
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 0 or nx < 0 or ny >= M or nx >= N or V[ny][nx] or S[ny][nx] == '.':
                    continue
                V[ny][nx] = 1
                Q.append((ny, nx))
        ans = max(ans, cnt)

print(component, ans, sep='\n')