# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 완전탐색 - 수 이어 붙이기
# 10 ~ 99의 수를 이어붙이는데 가장 작은 수 출력
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
cards = input().split()
permutations = permutations(cards, N)
# print(check)
answer = 10**20
for permutation in permutations:
	# print(permutation)
	pre = permutation[0]
	num = pre
	for p in permutation[1:]:
		if num[-1] == p[0]:
			num += p[1]
		else:
			num += p
   
	if answer > int(num):
		answer = int(num)
print(answer) # 순열 사용하고 카드 수가 8개라서 그냥 전체 검사로 해결

#해설1 : 순열을 구현해서 해결
N = int(input())
S = list(map(int, input().split()))
P = [0 for _ in range(8)]
used = [0 for _ in range(8)]
ans = 1e18

def Calculate(P):
    ret = P[0]
    for i in range(1, N):
        if ret % 10 == P[i] // 10:
            ret = ret * 10 + P[i] % 10
        else:
            ret = ret * 100 + P[i]
    return ret

def Permute(S, P, n):
    global ans
    if len(S) == n:
        ans = min(ans, Calculate(P))
        return
    for i in range(0, len(S)):
        if used[i]: continue
        used[i] = 1
        P[n] = S[i]
        Permute(S, P, n + 1)
        used[i] = 0
    
Permute(S, P, 0)
print(ans)

# 해설 2 : 순열 라이브러리 사용
# 내가 푼 풀이와 다른 점은 숫자의 상태에서 했다는 점
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1e18
for order in permutations(A, N):
    cur = order[0]
    for i in range(1, N):
        if cur % 10 == order[i] // 10:
            cur = cur * 10 + order[i] % 10
        else:
            cur = cur * 100 + order[i]
    ans = min(ans, cur)

print(ans)
