### 출처 : https://www.kaggle.com/code/agileteam/tutorial-t1-2-python/notebook
### # 2회 기출 유형 1번 ####
import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df.info())
# print(df.head())

### 1번
df_sort = df.sort_values('f5', ascending=False)
# print(df_sort.head(10))
df_ten_min = df_sort.head(10).f5.min()
# print(df_ten_min)
df_sort.iloc[:10, -1] = df_ten_min
# print(df_sort.head(10))
print(df_sort[df_sort.age >= 80].f5.mean())

## 2번
idx70 = int(len(df) * 0.7)
df70 = df.iloc[:idx70]
df30 = df.iloc[idx70:]
# print(df70.tail())
before = df70.f1.std()
df70['f1'] = df70.f1.fillna(df70.f1.median())
after = df70.f1.std()
# print('결측치 처리 전 표준편차 :', before)
# print('결측치 처리 후 표준편차 :', after)
print('두 표준편차 차이 :', before - after)

## 3번
std = df.age.std()
mean = df.age.mean()
out_b1 = mean - std*1.5
out_b2 = mean + std*1.5
# print(out_b1, out_b2)
# print(df.describe())
ans = df[(df.age>out_b2)|(df.age<out_b1)].age.sum()
print(ans)
