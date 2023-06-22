## 출처 : https://www.kaggle.com/code/agileteam/py-t1-14-2-expected-question/notebook

import pandas as pd
df = pd.read_csv('data/basic1.csv')

df = df.groupby(['city', 'f4'])[['f5']].mean()
df = df.sort_values('f5', ascending=False).head(7)
print(round(df['f5'].sum(), 2))

