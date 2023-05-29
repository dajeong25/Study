# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# [다시] 기초 자료구조의 구현과 응용 - 1차원 뿌요뿌요 게임

# 스택
# 뿌요의 색깔과 연속되는 개수 >> 스택에 쌍으로 
# 맨 위와 새로운 것이 색이 같으면 쌍을 스택에 담음. M개 이상이면 터짐
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip() + '!'

stack = [('', 1)]
for color in S:
	if stack[-1][0] != color:
		if stack[-1][1] >= M:
			top = stack[-1][0]
			# print(stack)
			while top == stack[-1][0]:
				stack.pop()
			# print(17, stack, top)
			
	if stack[-1][0] == color:
		stack.append((color, stack[-1][1]+1))
	else:
		stack.append((color, 1))

stack.pop()

if len(stack) > 1:
	print(''.join(i[0] for i in stack[1:]))
else:
	print('CLEAR!')


# 해설
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
Q = []
Q.append(('', 1))  # 처음에도 빈칸을 넣어줘서 indexerror를 일으키지 않도록 함

S += 'z'
for c in S:
    if Q[-1][0] != c:
        if M <= Q[-1][1]:
            top = Q[-1][0]
            print(16, Q)
            while top == Q[-1][0]:
                Q.pop()
            print(19, Q)
    if Q[-1][0] == c:
        Q.append((c, Q[-1][1] + 1))
    else:
        Q.append((c, 1))
print(24, Q)
Q.pop()

if len(Q) > 1:
    for c, n in Q:
        print(c, end='')
else:
    print("CLEAR!")
    
'''
10 3
ABCCCBBAAA

16 [('', 1), ('A', 1), ('B', 1), ('C', 1), ('C', 2), ('C', 3)]
19 [('', 1), ('A', 1), ('B', 1)]
16 [('', 1), ('A', 1), ('B', 1), ('B', 2), ('B', 3)]
19 [('', 1), ('A', 1)]
16 [('', 1), ('A', 1), ('A', 2), ('A', 3), ('A', 4)]
19 [('', 1)]
24 [('', 1), ('z', 1)]
CLEAR!
'''