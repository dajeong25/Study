# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반
# 시뮬레이션과 창의적 해결법 - 야구게임

# 기존의 야구게임 [저장]
'''
class BaseBall:
    player = 1
    outCount = 0
    strike = 0
    ball = 0

    def __init__(self):
        pass
    
    @classmethod
    def getStatus(cls): #현재 상태 출력
        s = f"{cls.outCount} 아웃, {cls.strike} 스트라이트, {cls.ball} 볼"
        return s
    
    @staticmethod
    def isStrike():
        import random
        return bool(random.randint(0,1))


##실행
print(f'\n=== {BaseBall.player}번째 선수 출격 ===')
while True:
    if BaseBall.isStrike():
        BaseBall.ball += 1
        print("\n공 던짐 => 볼!!")
    else:
        BaseBall.strike += 1
        print("\n공 던짐 => 스트라이크!!")
    print(BaseBall.getStatus())
    
    if BaseBall.ball == 4:
        print('1루 출루\n')
        BaseBall.strike = 0
        BaseBall.ball = 0
        BaseBall.player += 1
        print(f'=== {BaseBall.player}번째 선수 출격 ===')
        
    elif BaseBall.strike == 3:
        BaseBall.outCount += 1
        if BaseBall.outCount < 3:
            print("☞", BaseBall.outCount, ' 아웃 선수 교체\n')
            BaseBall.strike = 0
            BaseBall.ball = 0
            BaseBall.player += 1
            print(f'=== {BaseBall.player}번째 선수 출격 ===')
        elif BaseBall.outCount == 3:
            print("☞", BaseBall.outCount)
            print("쓰리아웃! 공수교체!!")
            break
'''
