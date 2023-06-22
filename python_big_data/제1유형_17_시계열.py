## 출처 : https://www.kaggle.com/code/agileteam/py-t1-17-1-expected-question/notebook
import pandas as pd
df = pd.read_csv('data/basic2.csv')
# print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['dayofweek'] = df['Date'].dt.dayofweek
# print(df.head())
ans = df[(df.year==2022)&(df.month==5)].Sales.median()
print(ans)

# T1 - 22 : weekly
df_w = df.resample('W', on='Date').sum()
# print(df_w.head())
w_max = df_w.Sales.max()
w_min = df_w.Sales.min()
print(w_max - w_min)