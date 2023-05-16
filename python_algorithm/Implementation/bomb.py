## 다시 하기(현재 코드는 숫자부분에 에러 발생함 수정 필요)
# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 폭탄 구현
import sys
input = sys.stdin.readline
n, k = map(int, input().split()) # 각각의 원소로 받을 때는 list 필요 없음
	# 위, 왼, 오, 아래
dx = [0, -1, 1, 0] 
dy = [-1, 0, 0, 1]

ground = [[0 for i in range(n)] for j in range(n)]
for _ in range(k):
	y, x = map(int, input().split()) # 각각의 원소로 받을 때는 list 필요 없음
	y, x = y-1, x-1
	ground[y][x] += 1
	for i in range(4): # 이전의 4개의 if문 아닌 좌표 위치를 받고 이동하면서 더해야 에러가 없음 + 효율적
		ny = y + dy[i]
		nx = x + dx[i]
		if ny<0 or ny>=n or nx<0 or nx>=n:
			continue
		ground[ny][nx] += 1

print(sum(sum(x) for x in ground))
