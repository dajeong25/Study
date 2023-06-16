# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

a = pd.read_csv('data/blood_pressure.csv', index_col=0)


# 사용자 코딩
# print(a.head())
# print(a.info())
# print(a.describe())
# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출

# 1번
import numpy as np
n = len(a)
diff = np.sum(a.bp_after - a.bp_before)
ans_mean = round(diff/n, 2)
print(ans_mean)

# 2번
from scipy.stats import ttest_rel
t, p = ttest_rel(a.bp_after, a.bp_before, alternative='less')
t = round(t, 4)
print(t)

# 3번
p = round(p, 4)
print(p)

# 4번
print('p-값은', p, '이다. 그러므로, p-값이 유의수준보다 작다. 그러므로 귀무가설을 기각한다.')
