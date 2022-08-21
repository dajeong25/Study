#2차원 리스트를 만들어 "학생별" 총점, 평균 구하기
kor_score = [49, 79, 20, 100,80] 
math_score = [43, 59, 85, 30, 90] 
eng_score = [49, 79, 48, 60, 100] 
midterm_score = [kor_score, math_score, eng_score]

mid_add = [0, 0, 0, 0, 0]

for row in midterm_score:
    mid = 0 
    for col in row:
        mid_add[mid] += col
        mid += 1

for i in range(len(mid_add)):
    print(f'학생{i+1} 총점: {mid_add[i]}, 평균: {mid_add[i]//3}')


''' ##그 외 답안
total = [0,0,0,0,0]  #총점을 저장할 리스트 초기화
for  subject in midterm_score :  
    idx = 0
    for  jumsu in subject :
        total[idx] += jumsu
        idx+=1

print("총점 : ", total)
print("평균 : ", end=" ")
for jumsu in total:
    print(jumsu/3, end=" ")

# -----------------------------------------------------------------------
student_mean = []
for col in range(0, 5) :
    sum_score = 0
    for row in range (0, 3): 
        sum_score += midterm_score[row][col]
    student_mean.append(sum_score/3)   

for i in range(0, 5) :
    print("{}번 학생의 평균 점수 : {}점".format(i+1,student_mean[i]))

# ----------------------------------------------------------------------
x= []     #총점 저장 리스트
y= []     #평균 저장 리스트
for i in range(5):
    total_score = kor_score[i] + math_score[i] + eng_score[i]
    x.append(total_score)
    y.append(total_score / 3)
    
print("각 학생들의 총점은", x)
print("각 학생들의 평균은", y)

'''