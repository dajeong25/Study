# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그리디 알고리즘, 원인과 결과 찾기 - 구름 스퀘어
# 회의실 배정 문제
# : 시간이 겹치지 않게 최대한 많은 행사 열 수 있도록하면서
#   가장 많은 행사의 수 구하기
# 완전탐색 == 2**n개 == 20만개이므로 불가능
# 그리디 = 적절한 기준을 세워봄
'''
1. 시작 시간이 빠른 순
    > 1 10 이 있으면 무용지물
2. 행사 시간이 짦은 순
    > 시간이 겹친다면 불가능 
    > 1 3 / 3 4 / 4 6 : 종료 후 정리 1시간이 필요하기에 독립적이지 못함
3. 종료시간이 빠른 순
    > K -> K+a >> 최소로 가능함(최적해 보장)
    > 즉, 1개의 회의실에 여러개의 회의가 열린다면
      종료 시간 순으로 선택하면 가장 많은 희의 개최 가능
으로 정렬
'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())

times = [list(map(int, input().split())) for _ in range(N)]
times = sorted(times, key=lambda x: [x[1], x[0]])
# print(times)
cnt = 1
s1, e1 = times[0]
for s,e in times[1:]:
	if e1+1 <= s:
		cnt += 1
		s1, e1 = s, e
		# print(s, e)
print(cnt)


### 해설
import sys
input = sys.stdin.readline

N = int(input())
events = []
for _ in range(N):
    s, e = map(int, input().split())
    events.append([s, e])
    
events.sort(key=lambda x : (x[1], x[0]))
count = end = 0
for s, e in events:
    if s > end:
        count += 1
        end = e
        
print(count)