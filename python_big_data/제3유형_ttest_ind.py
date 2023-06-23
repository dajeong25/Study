# 출처 : https://www.kaggle.com/code/agileteam/t3-ttest-ind/notebook

## T3 : ttest_ind
group1 = [36.8, 36.7, 37.1, 36.9, 37.2, 36.8, 36.9, 37.1, 36.7, 37.1] #복용
group2 = [36.5, 36.6, 36.3, 36.6, 36.9, 36.7, 36.7, 36.8, 36.5, 36.7] #안함

# your code
from scipy import stats as ss
s, p = ss.ttest_ind(group1, group2)

# 1 검정통계량
print(s)

# 2 p-value
print(p)

# 검정결과
alpha = 0.5
if p >= alpha:
    print('채택')
else :
    print('기각')