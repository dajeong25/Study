##### 다시 풀어보기!! #####

# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 소수 위치 더하기

def isPrime(num):
	for i in range(2, int(num**(1/2)+1)): #소수판별 시 실질적으로는 n**(1/2)까지만 봐도 판별 가능!!
		if num % i == 0 :
			return False
	return True

n = int(input())
a = list(map(int, input().split()))
answer = 0
for i in range(2, n+1):
	if isPrime(i):
		answer += a[i-1]
print(answer)

# 위 방법의 시간 복잡도는 O(N^3/2)
# 이 방법도 좋지만 소수 판별 시에는
# <에라토스테네스의 체>를 사용하는 것이 더 효율적!
# 즉, 어떤 수가 배수인지 세는것이 훨씬 쉬움

# 슈도코드
# 초기에는 모두 소수일 수 있다고 가정하고 list 담기
# for문에서 소수가 아니라고 판정 된 수는 건너뜀
#       소수이면 리스트 추가
#       추가한 소수의 배수면 제외
# 소수 리스트 반환
#  >> 이경우 시간 복잡도 O(NloglogN)