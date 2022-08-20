#outer 반복문은 행 수, inner 반복문은 열 수 
#5행4열  
'''
(0, 0) (0, 1) (0, 2) (0, 3) 
(1, 0) (1, 1) (1, 2) (1, 3) 
(2, 0) (2, 1) (2, 2) (2, 3) 
(3, 0) (3, 1) (3, 2) (3, 3) 
(4, 0) (4, 1) (4, 2) (4, 3) '''
for row in range(5):
    for col in range(4):
        print("({0}, {1})".format(row, col), end=" ")
    print()
print()

#tuple 사용
for row in range(5):
    for col in range(4):
        a = (row, col)
        print(a, end=" ")
    print()

'''
for  row in range(0, 5) :
    for col in range(0, 4):
        data = (row, col)  #tuple객체로 만듬
        print(data ,   end=" ") 
    print()    
'''


#정사각형 별로 출력
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()


'''
for  row in range(0, 5) :
    for col in range(0, 5):         
        print("*" ,   end=" ") 
    print()   
'''


#별 출력
'''
*  
* *  
* * *   
* * * *  
* * * * * 
'''
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()


##위의 별 출력을 재귀 호출로 한다면?
'''어렵구만.. 다시 풀어보기!!
★
★★ 
★★★ 
★★★★
★★★★★
'''
def star(num):
    if num > 0:
        star(num-1)
        print("★ " * num)

print(star(5))


'''
for y in range(6) : #1~10까지 반복한다.
    for x in range(y) : # 이 코드를 좀 검토해주세요 
        print('*', end=' ') # * 문자를 출력한다.
    print() # 개행한다.

for  row in range(0, 5) :
    for col in range(0, row+1):         
        print("*" ,   end=" ") 
    print()  
'''

#*을 반대로 출력하려면?
''' 
* * * * *     (1, 5)
* * * *       (2, 4)
* * *         (3, 3)
* *           (4, 2)
*             (5, 1) '''
for row in range(5):
    for col in range(5-row):
        print("*", end=" ")
    print()


'''
for  row in range(0, 5) :
    for col in range(5-row):         
        print("*" ,   end=" ") 
    print()  
'''


# *아래의 반대로 출력하려면? outer for 문 내부에 2개의 for 문 사용
'''
* * * * *    (1, 0, 5)
  * * * *    (2, 1, 4)
    * * *    (3, 2, 3)
      * *    (4, 3, 2)
        *    (5, 4, 1)'''
for row in range(5):
    for col in range(row):
        print(" ", end=" ")
    for col in range(5-row):
        print("*", end=" ")
    print()


'''
for row in range(1, 6) :
    for col in range(1, row) :
        print(" ", end=" ")
    for col in range(6, row, -1) :  #range(start, end, stepby)
        print("*", end=" ")            
    print()

'''

'''
        *    (5, 4, 1)
      * *    (4, 3, 2)
    * * *    (3, 2, 3)
  * * * *    (2, 1, 4)
* * * * *    (1, 0, 5)'''
for row in range(1, 6):
    for col in range(5-row):
        print(" ", end=" ")
    for col in range(row):
        print("*", end=" ")
    print()

