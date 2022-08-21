'''Q8>4행 3열의 2차원리스트 선언하고 아래의 값으로 초기화 한 후 
차례대로 출력한 후 리스트의 모든 값을 더한 결과를 출력하는 프로그램을 작성하시오.
[[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
'''

double_list = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
list_sum = 0

for row in double_list:
    count = 0
    for col in row:
        count += 1
        list_sum += col
        if count == 3:
            print(col)
        else:
            print(col, end=' ')

####### 인덱스 활용 출력 #######
for row in range(len(double_list)):
    for col in range(len(double_list[row])):
        print(double_list[row][col], end=' ')
        list_sum += double_list[row][col]
    print()

print("\n행렬의 합:", list_sum)


'''#그 외 답안
nums = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
sum = 0
for rows in nums:
    for cols in rows:
        print(cols, end=' ')
        sum += cols
    print()
print(sum)

#답안2
listData = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
sum_val = 0
for row in range(len(listData)) :
    for col in range(len(listData[row])):
        print(listData[row][col], end=" ") # 차례대로 출력
        sum_val += listData[row][col] # 총합 계산
    print()
print("총합 :", sum_val) # 총합 출력
'''
