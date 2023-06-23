# 출처 : https://www.kaggle.com/code/agileteam/t3-correlation/notebook

#### T3 - correlation
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.info())
# print(df.head())
corr_df = df.iloc[:, :2]
# print(corr_df.head())
ans = round(corr_df.corr().iloc[0,1], 2)
print(ans)
