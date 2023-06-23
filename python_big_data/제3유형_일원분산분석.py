# 출처 : https://www.kaggle.com/code/agileteam/t3-anova/notebook

#### T3 - anova

# 각 그룹의 데이터
groupA = [85, 92, 78, 88, 83, 90, 76, 84, 92, 87]
groupB = [79, 69, 84, 78, 79, 83, 79, 81, 86, 88]
groupC = [75, 68, 74, 65, 77, 72, 70, 73, 78, 75]

# your code
from scipy import stats as ss
n = 30
alpha = 0.05
s, p = ss.f_oneway(groupA, groupB, groupC)

print(round(s, 2))
print(round(p, 6))

if p >= alpha:
    print('채택')
else:
    print('기각')
