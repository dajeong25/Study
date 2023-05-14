## 다시 하기
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
def fail():
    for i in range(4):
        # 상태가 Fail인 자리만 작업을 수행합니다.
        if result[i] != 2:
            continue
        # 조건을 만족하는 값이 나올 때까지 아래 과정을 반복합니다.
        while True:
            # 현재 자리의 값을 1 증가시킵니다.
            # 값을 바로 대입하지 않고, 현재 입력의 다른 자리에 해당 값이 존재하는지를 먼저 판단합니다.
            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                break

def ball():
    if 1 not in result:
        return
    pos = []
    value = []
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])
    for i in range(len(pos)):
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]

make_input_count = 0
while True:
    make_input_count += 1
    result = [2, 2, 2, 2]
    # user_input과 answer이 같은 경우는 게임이 종료되는 조건에 해당됩니다.
    if user_input == answer:
        # 따라서 과정을 수행한 횟수를 출력하고 루프를 탈출합니다.
        print(make_input_count)
        break

    # 입력의 첫째 자리부터 순서대로 보면서 상태를 판단합니다.
    for i in range(4):
        # 헌재 값이 answer에 없는 경우는 Fail에 해당합니다.
        # 앞서 상태의 기본값을 Fail로 설정했기 때문에 그냥 넘어가면 됩니다.
        if user_input[i] in answer:
            # 위치까지 같은 경우는 Strike에 해당합니다.
            if user_input[i] == answer[i]:
                result[i] = 0
            # 그렇지 않은 경우는 Ball에 해당합니다.
            else:
                result[i] = 1
                
