# [다시]
# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반'
# 사후 - 정렬
# 1차시도 : defaultdict와 Counter로 센 다음 추출 시 for&if문 사용 -> 시간초과..
# 라이브 후 2차 시도 : filter 사용 -> 내장함수 사용 시 정말 빠르고 간결함

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

e = defaultdict(int)
for _ in range(M):
	events = list(map(int, input().split()))
	for event in events[1:]:
		e[event] += 1

result = sorted(e.items(), key=lambda x: (x[1], x[0]), reverse=True)
answer = list(filter(lambda x : x[1]==result[0][1], result))

#방법1
# print(' '.join(str(x[0]) for x in answer)) 

#방법2
for i in answer:
    print(i[0], end=' ')
    