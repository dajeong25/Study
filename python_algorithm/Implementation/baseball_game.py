## 다시 하기(현재 코드는 숫자부분에 에러 발생함 수정 필요)
# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 야구게임

# 슈도코드
'''
- strike, ball, fail 처리 기능
- fail 처리 기능
- ball 처리 기능

1. 값을 list에 저장해서 관리하기 편하게 저장하기
2. strike, ball, fail 판단 : result list를 생성해서 각 자리의 상태 관리
    1) result 모든 상태 fail로 저장
    2) 첫번째 자리부터 정답 포함되는지 판단. 포함이면 3번으로 아니면 pass
    3) 정답이라면 strike, 아니면 ball.
3. fail 처리 
    1) 입력 첫번째부터 순서대로 작업
    2) fail 자리만 수행
    3) 현재값 1증가 10 나누기
    4) 겹치지 않을 때까지 반복
4. ball 처리 : 입력값을 오른쪽으로 옮기면서 정답 찾기
'''
answer = list(map(int, input()))
start = list(map(int, input()))

def fail():
	for i in range(4):
		if save[i] != 0:
			continue
		while True:
			temp = (start[i] + 1) % 10
			out = temp not in start
			start[i] = temp
			if out:
				break

def ball():
	if 1 not in save:
		return
	pos = []
	value = []
	for i in range(4):
		if save[i] != 2:
			pos.append(i)
			value.append(start[i])
	for i in range(len(pos)):
		if i == 2:
			start[pos[i]] = value[-1]
		else:
			start[pos[i]] = value[i - 1]

cnt = 0
while True:
	cnt += 1
	save = [0,0,0,0] #s=2, b=1, f=0  >> 이 순서를 역으로 하면 바로 통과
	if answer == start:
		print(cnt)
		break
		
	for i in range(4):
		if start[i] in answer: #strike
			if start[i]==answer[i]:
				save[i]=2
			else:
				save[i]=1
	fail()
	ball()
	