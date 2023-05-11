# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 소개팅해주기
# 2차시도
import sys
input = sys.stdin.readline

n = int(input())
s_list = list(map(int, input().split()))
s_list.sort()           #점수를 정렬해서
answer = s_list.copy()
for s in s_list[:n//2]: #절반만 확인
	if s in answer and -s in answer: #answer에 둘다 있으면 제거
		answer.remove(s)
		answer.remove(-s)
print(sum(answer)) #남은 정답의 합계 구했는데... timeout.

# 전체를 다 안 돌고 절반만 돌렸는데도 시간초과라는 건,
# 복사를 하고 삭제를 하는 과정 자체가 시간이 많이 걸리는 걸까?
# 그렇다면 제거를 하는게 아니라 양쪽 끝에서 0점을 계산하는 방식으로 가야하는 건가?