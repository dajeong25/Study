# 출처 : https://www.datamanim.com/dataset/practice/ex5.html

# 5회 기출 변형 - 작업 3유형 ★★★★★
## 95% 신뢰구간
import pandas as pd
from scipy import stats as ss

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p3_1.csv')
# print(df.head())
# print(df.info())

#3-1-1
df_mean = round(df.height.mean(),3)
print(df_mean)

#3-1-2
n = len(df.height)
confidence_level = 0.95 #신뢰수준
ddof = n-1 # 자유도
t_value = round(ss.t.ppf((1+confidence_level)/2, ddof),4) # ss.t.ppf(유의수준, 자유도)
# print((1+confidence_level)/2, 1-0.025 ) 
# # 0.975 0.975 >> 양쪽이니까 한쪽의 t값 가져오기 위함
print(t_value)

# 3-1-3
## 신뢰구간 : t.interval(신뢰도, 자유도, loc=샘플평균, scale=샘플표준오차)
std_error = df.height.std()/n**0.5 #표준오차 : std/루트(샘플사이즈)
interval = ss.t.interval(confidence_level, ddof, loc=df_mean, scale=std_error)
lower = round(interval[0],3)
upper = round(interval[1],3)
print(lower, upper)


import pandas as pd
import numpy as np
from scipy import stats as ss
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p3_2.csv')
# print(df.head())
# print(df.info())

## 3-2-1
# print(df.ID.unique())
a = df[df.ID == 'A'].value
b = df[df.ID == 'B'].value
c = df[df.ID == 'C'].value
# print(a,b,c)
s,p = ss.kruskal(a,b,c)
print(round(s, 3))

# 3-2-2
# p = round(p,3)
print(p)
if p > 0.5 :
    print('채택') #귀무가설 기준
else:
    print('기각')
