## 출처 : https://www.kaggle.com/code/agileteam/py-t1-3-map-expected-questions/notebook
import pandas as pd

df = pd.read_csv('data/basic1.csv')
# print(df.head())
# print(df.isnull().sum())
# print(len(df.f1), len(df.f1)*0.8)

# f3은 삭제
df.drop('f3', inplace=True, axis=1)

# f1 city별 평균값 대체
temp = df.groupby('city').f1.median()
# print(dict(temp))

df['f1'] = df['f1'].fillna(df['city'].map(dict(temp)))
# print(df.head())

print(df.f1.mean())