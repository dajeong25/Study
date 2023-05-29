# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# [다시] 기초 자료구조의 구현과 응용 - 1차원 뿌요뿌요 게임

# 스택
# 뿌요의 색깔과 연속되는 개수 >> 스택에 쌍으로 
# 맨 위와 새로운 것이 색이 같으면 쌍을 스택에 담음. M개 이상이면 터짐
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip() + '!'

stack = [(S[0], 1)]
for color in S[1:]:
	if stack[-1][0] == color:
		stack.append((color, stack[-1][1]+1))
	else:
		if stack[-1][1] >= M:
			for i in range(stack[-1][1]):
				stack.pop()
			if len(stack) == 0 and color == S[-1]:
				break
			else:
				if stack[-1][0] == color:
					stack.append((color, stack[-1][1]+1))
				else:
					stack.append((color, 1))
		else:
			stack.append((color, 1))
	
if stack:
	print(''.join(i[0] for i in stack[:-1]))
else:
	print('CLEAR!')
