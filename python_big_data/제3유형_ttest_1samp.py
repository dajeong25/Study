# 출처 : https://www.kaggle.com/code/agileteam/t3-ttest-1samp/notebook

#### T3 - ttest_1samp

# 데이터
scores = [75, 80, 68, 72, 77, 82, 81, 79, 70, 74, 76, 78, 
          81, 73, 81, 78, 75, 72, 74, 79, 78, 79]

## your code
from scipy import stats as ss
alpha = 0.05
n = len(scores)
mu = 75

# 대립 가설을 정의합니다. 다음 옵션을 사용할 수 있습니다(기본값은 '양면').
# 'two-sided': 표본의 기본 분포의 평균이 주어진 모집단 평균( popmean ) 과 다릅니다.
# 'less': 표본의 기본 분포의 평균이 주어진 모집단 평균( popmean ) 보다 작습니다.
# 'greater': 표본의 기본 분포의 평균이 주어진 모집단 평균( popmean ) 보다 큽니다.
s, p = ss.ttest_1samp(scores, mu, alternative='greater')
print(s)
print(p)

if p >= alpha:
    print('채택')
else:
    print('기각')
