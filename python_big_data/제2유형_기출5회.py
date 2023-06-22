## 출처 : https://www.datamanim.com/dataset/practice/ex5.html

# 5회 기출 변형 - 작업 2유형 ★★★★★
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_train_.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_test_.csv')
# print(train.info())
# print(test.info())

y = train.loc[:,'price']
X = train.drop(['price', 'ID'], axis=1)
test_id = test.pop('ID')

dum_X = pd.get_dummies(X)
dum_test = pd.get_dummies(test)
dum_test = dum_test.reindex(columns=dum_X.columns, fill_value=0)
print(dum_X.shape)
print(dum_test.shape)
