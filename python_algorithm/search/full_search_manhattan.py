# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 완전탐색 - 맨하튼거리
# 1차 - 모름로꼴 전체 탐색 > 경우의 수가 많아서 pass
# 2차 - 좌표를 가져와서 맨하튼 거리 측정
# 3차 - 문제를 제대로 읽지 않은 자의 최후.. 
# 	>> 개미가 진딧물을 얻을 수 있으면 ok. 
# 		그 개미가 몇개의 진딧물을 받을 수 있는 지는 상관없음.

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

ants, foods = [], []
for y in range(N):
	ground = list(map(int, input().rstrip().split()))
	for x in range(N):
		if ground[x] == 1:
			ants.append([y,x])
		elif ground[x] == 2:
			foods.append([y,x])
		else:pass

answer = 0
for y1, x1 in ants:
	for y2, x2 in foods:
		if (abs(y1-y2) + abs(x1-x2)) <= M:
			answer += 1
			break # 이걸 추가해야 개미 수가 중복 안됨!!

print(answer)