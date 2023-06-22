## 출처 : https://www.kaggle.com/code/agileteam/py-t1-21-expected-question/notebook
import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df.isnull().sum())
# print(df.shape)

outlier = df[~(df.age <= 0)&(df.age == round(df.age, 0))]
# print(outlier.shape)
# print(outlier.head())

outlier['range'] = pd.qcut(outlier.age, q=3, labels=['group1','group2','group3'])
# print(outlier.range.value_counts())
ans = outlier.groupby('range').age.median().sum()
print(int(ans))
