# 출처 : DMOJ, ECOO '17 R3 P1 - Baker Brie
# 총 매출 13의 배수 = 매출//13의 보너스 지급
# 하루 매출 13의 배수의 모든 가맹점 매출//13의 보너스 지급
lst = input().split()
franchisees = int(lst[0])
days = int(lst[1])

grid = []

for i in range(days):
    row = input().split()
    for j in range(franchisees):
        row[j] = int(row[j])
    grid.append(row)

bonuses = 0

for row in grid:
    total = sum(row)
    if total % 13 == 0:
        bonuses = bonuses + total // 13

for col_index in range(franchisees):
    total = 0
    for row_index in range(days):
        total = total + grid[row_index][col_index]
    if total % 13 == 0:
        bonuses = bonuses + total // 13

print(bonuses)

# 굳이 이차원리스트로 안하고 바로 한다면?
# franchise, days = map(int, input().split())
# sold = []
# total = 0
# for _ in range(days):
#     a_day = list(map(int, input().split()))
#     total += sum(a_day)
