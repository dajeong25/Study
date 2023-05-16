# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 완전탐색 - 맨하튼거리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ground = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 수색범위는 마름모모양 O(M^2)
# 시간복잡도 O(N^2 M^2)

answer = 0
for y in range(N):
	for x in range(N):
		if ground[y][x] == 1:
			print('---', y, x, '----')
			for ny in range(1, M+1):
				for nx in range(1, M+1):
					dy = [-ny, 0, 0, ny]
					dx = [0, -nx, nx, 0]
					
					for i in range(4):
						my = y + dy[i]
						mx = x + dx[i]
						if my<0 or my>=N or mx<0 or mx>=N:
							continue
						print(ny, nx, my, mx, ground[my][mx])
						if ground[my][mx] == 2:
							answer += 1

print(answer//2)
