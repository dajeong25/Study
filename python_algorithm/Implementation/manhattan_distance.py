# 출처 : 멀티잇 코딩테스트 러닝클래스'Python 5월반

# ab cd / ac bd / ad bc
# 경우의 수가 적어서 수작업으로 나열
a,b,c,d = map(int, input().split())
answer = max(abs(a-b)+abs(c-d), abs(a-c)+abs(b-d), abs(a-d)+abs(b-c))
print(answer)

'''
이렇게 말고 완전탐색의 방법도 있지만, 수학적으로 효율적으로 접근한다면?
>> |x2 - x1| + |y2 - y1| 에서 절대값 제거
>> x2-x1+y2-y1 
>> x2 +y2 -x1 -y1 
  큰값-작은값이 가장 큰 맨하탄 거리가 나오는 것을 알 수 있음
'''
answer = list(map(int, input().split()))
answer.sort()
print((answer[3]-answer[1])+(answer[2]-answer[0])) #정렬 후 큰수에서 작은수를 빼기 때문에 절대값은 할 필요 없음
