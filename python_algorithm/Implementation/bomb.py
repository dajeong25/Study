## 다시 하기(현재 코드는 숫자부분에 에러 발생함 수정 필요)
# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 폭탄 구현

n, k = list(map(int, input().split()))

ground = [[0 for i in range(n)] for j in range(n)]
for _ in range(k):
	y, x = list(map(int, input().split()))
	y, x = y-1, x-1
	ground[y][x] += 1
	if x-1>=0 :
		ground[y][x-1] += 1
	if x+1<k:
		ground[y][x+1] += 1
	if y-1>=0:
		ground[y-1][x] += 1
	if y+1<k:
		ground[y+1][x] += 1

print(sum(sum(x) for x in ground))