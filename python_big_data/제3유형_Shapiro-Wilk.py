# 출처 : https://www.kaggle.com/code/agileteam/t3-shapiro-wilk/notebook

#### T3 - Shapiro-Wilk

# 데이터
data = [75, 83, 81, 92, 68, 77, 78, 80, 85, 95, 79, 89]

# your code
from scipy import stats as ss
s, p = ss.shapiro(data)
print(s)
print(p)
if p >= 0.05:
    print('채택') #정규분포를 따른다
else:
    print('기각')
