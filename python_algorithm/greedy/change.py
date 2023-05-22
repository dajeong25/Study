# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 그리디 알고리즘, 원인과 결과 찾기 - 거스름돈

charge = int(input())

coins = [40,20,10,5,1]

n = 0
for coin in coins:
	n += charge // coin
	charge = charge % coin

print(n)
