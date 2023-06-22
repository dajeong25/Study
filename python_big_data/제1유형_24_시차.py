## 출처 : https://www.kaggle.com/code/agileteam/t1-24-time-series5-lagged-feature/notebook
import pandas as pd
df = pd.read_csv('data/basic2.csv')
# print(df.info())
# print(df.isnull().sum())

df['pre_PV'] = df['PV'].shift(1)
df['pre_PV'] = df['pre_PV'].fillna(method='bfill')
df['pre_PV'] = df['pre_PV'].astype('int64')
print(df.info())

ans = df[(df.Events == 1)&(df.Sales <=1000000)].pre_PV.sum()
print(ans)
