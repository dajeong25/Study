# 출처 : https://www.kaggle.com/code/agileteam/t3-example/notebook

## T3 : 대응(쌍체)표본 t-검정

import pandas as pd
df = pd.read_csv("data/high_blood_pressure.csv")

# your code

#### 1번 ####
# print(df.info())
# print(df.head())
n = len(df)
df['bp_diff'] = df.bp_post - df.bp_pre
x_mean = round(df.bp_diff.mean(), 2)
print(x_mean)

#### 2번 ####
from scipy import stats as ss
s, p = ss.ttest_rel(df['bp_post'], df['bp_pre'], alternative='less')
# print(df.describe())
s = round(s, 4)
print(s)

#### 3번 ####
p = round(p, 4)
print(p)

#### 4번 ####
if p >= 0.5:
    print('채택')
else :
    print('기각')
