## 출처 : https://www.datamanim.com/dataset/practice/ex5.html

# 5회 기출 변형 - 작업 1유형
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 1번
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_1_.csv')
df_filter = df[(df['20L가격']!=0)&(df['5L가격']!=0)].copy()
# print(df_filter.head())
df_filter['차이가격'] = df['20L가격'] - df['5L가격']
ans1 = df_filter.groupby('시도명').차이가격.mean().max()
print(int(ans1))

# 2번
df2 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_2_.csv')
# print(df2.info())
# print(df2.head())
df2['BMI'] = df2['weight(kg)'] / ((df2['height(cm)']/100)**2)

def check(x):
    if x>=25:
        return '초고도비만'
    elif x>=23:
        return '비만'
    elif x>=18.5:
        return '정상'
    else:
        return '저체중'

df2['bmi_check'] = df2['BMI'].map(lambda x : check(x))
print(df2[(df2.bmi_check=='초고도비만')|(df2.bmi_check=='저체중')].BMI.count())

# 3번 ★★★★★
df3 = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_3.csv')
# print(df3.info())
# print(df3.head())

df3['순유입인원'] = \
    df3[[x for x in df3.columns if '전입' in x]].sum(axis=1) - \
    df3[[x for x in df3.columns if '전출' in x]].sum(axis=1)
# print(df3.head())
ans3 = df3.groupby('년도')['순유입인원'].max().sum()
print(ans3)
