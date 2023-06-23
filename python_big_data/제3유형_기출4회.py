### 출처 : https://www.datamanim.com/dataset/practice/ex4.html
### 기출 4회 제3유형 ####
import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p3_1_.csv')
print(df.head())

## 1번
g = df.groupby('학과').count().mean()
print(round(g,3))

## 2번
from scipy import stats as ss
s, p = ss.chi2_contingency(df['학과'], df['성별'])
print(s, p)
