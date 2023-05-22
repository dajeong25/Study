# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그리디 알고리즘, 원인과 결과 찾기 - 거스름돈

charge = int(input())

coins = [40,20,10,5,1]

n = 0
for coin in coins:
	n += charge // coin
	charge = charge % coin

print(n)

'''
coding test Tip
: 동전 교환 외의 그리티 알고리즘 해당 유형
: 상황이 명확하기 때문에 해결하기 쉬운 편

1. 회의실 배정 문제
2. Fractional Knapsack, 분할 가능한 배낭채우기
3. 다익스트라, 프림, 크루스칼 등의 비용을 최적하는 그래프 이론
'''