## 출처 : https://www.kaggle.com/code/agileteam/py-t1-4-expected-questions/notebook

import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df.head())

enfj_std = df[(df.f4 == 'ENFJ')]['f1'].std()
infp_std = df[(df.f4 == 'INFP')]['f1'].std()
print(abs(enfj_std - infp_std))
