### 출처 : https://www.datamanim.com/dataset/practice/ex4.html
### 기출 4회 제1유형 ####
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_1.csv')
# print(df.info())
# print(df.head())

## 1번
df['Temperature'] = df.Temperature.apply(lambda x : x.replace('*', '')).astype('float')
# print(df.info())
q1 = df.Temperature.quantile(0.25)
q3 = df.Temperature.quantile(0.75)
ans = round(q3 - q1, 2)
print(ans)

## 2번
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_2.csv')
# print(df.head(5))
# print(df.info())
df['rate'] = df['Likes'] / df['Comments']
ans = df[(df.rate >= 20)&(df.Keyword=='minecraft')].Views.mean()
print(int(ans))

## 3번
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_3.csv')
# print(df.head(5))
# print(df.info())
# print(df.date_added.unique())
df['date_dt'] = pd.to_datetime(df.date_added)
# print(df.head())
ans = df[(df.date_dt.dt.strftime('%Y-%m')=='2018-01')&(df.country=='United Kingdom')].shape
print(ans[0])
