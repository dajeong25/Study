# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 기초 자료구조의 구현과 응용 - 스택구조

N, K = map(int, input().split())

stack = []
for _ in range(N):
	cmd = input()
	if "push" in cmd and len(stack) < K:
		cmd, n = cmd.split()
		stack.append(int(n))
	elif "push" in cmd and len(stack) >= K:
		print("Overflow")
	elif "pop" in cmd and len(stack) > 0:
		print(stack.pop())
	elif "pop" in cmd and len(stack) == 0:
		print("Underflow")
	else:pass
	