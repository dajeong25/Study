# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 기초 자료구조의 구현과 응용 - 체크카드

# deposit : 계좌 입금
# pay 결제 - deposit보다 금액 크면 결제 안됨
# reservation 계좌 결제, 금액이 크거나 대기목록에 다른 거래 있으면 대기 목록에 추가됨
# 대기 : 결제 가능해지는 즉시 차감된 후 목록에서 삭제됨
import sys
from collections import deque
input = sys.stdin.readline
#잔액 거래횟수
N, M = map(int, input().split())
wait = deque()
for _ in range(M):
	w, num = input().split()
	num = int(num)

	while True:
		if len(wait) > 0 and N >= wait[0]:
			N -= wait.popleft()
		else:
			break
	
	if w == 'deposit':
		N += num
	elif w == 'pay':
		if N >= num:
			N -= num
	else:
		if len(wait)==0 and N >= num:
			 N -= num
		else:
			wait.append(num)

while True:
	if len(wait) > 0 and N >= wait[0]:
		N -= wait.popleft()
	else:
		break
print(N)
