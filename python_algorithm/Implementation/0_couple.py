# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 소개팅해주기
# 3차시도 : 단순히 리스트의 양 끝단에서 비교하는 로직으로 수정!
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()
answer = 0
left = 0   #음수
right = n-1  #양수

# 처음엔 n//2로 했다가 fail.
# 값이 한쪽으로 변향되게 더 많은 경우는 정가운데 값이 확인이 아는 경우가 있음
for _ in range(n//2+1):      # n//2 +1 로 한번더 검사해야하는 것이 핵심
	if -s[left] == s[right]: # 양끝이 동일하면 pass
		left += 1
		right -= 1
	elif -s[left] > s[right]: # 음수가 더 크면 음수만 위치 변경해서 양수값과 맞춰주기
		answer += s[left]
		left += 1
	elif -s[left] < s[right]: # 양수가 더 크면, 양수 위치 변경
		answer += s[right]
		right -= 1
	else: pass
print(answer)

#  정답 1: hash 기반 - dict에 한쪽 기록하고 없는 값만 추가
#  정답 2: 절대값 개수 이용 - 절대값 개수를 센 후 절대값이 1번만 등장한 경우 정답.
#  정닶 3: n-n=0, 고로 전체 더하면 정답!! 와.... 정말 대박인 문제...ㄷㄷㄷㄷ