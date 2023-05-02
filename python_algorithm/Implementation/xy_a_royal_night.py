'''
출처 [저서] : 이것이 취업을 위한 코딩테스트다 with 파이썬

## 왕실의 나이트 ##
- 수평 2칸 > 수직 1칸
- 수직 2칸 > 수평 1칸
'''
# (x, y) L R U D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
steps = [(-1,2), (1, 2), (-1,-2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)] #나이트 이동 방향

xy = input()

# x의 알파벳을 수작업으로 지정 후 변환
x_list = ['a','b','c','d','e','f','g','h']
now = list(map(int, [x_list.index(xy[0]), xy[1]]))

# 교재: ord로 유니코드 변경하여 변환 good!
# now = [int(ord(xy[0]))-int(ord('a'))+1, int(xy[1])]

cnt = 0
for step in steps:
    x = now[0] + step[0]
    y = now[1] + step[1]
    if x>0 and y>0 and x<9 and y<9: # 모두 (0 <x, y< 9)면 이동 가능한 위치
        cnt += 1
print(cnt)
