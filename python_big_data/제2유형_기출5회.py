## 출처 : https://www.datamanim.com/dataset/practice/ex5.html

# 5회 기출 변형 - 작업 2유형 ★★★★★
# RMSE는 예측값의 차이가 작을수록 성능이 더 좋음
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_train_.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_test_.csv')
# print(train.info())
# print(test.info())

y = train.loc[:,'price']
X = train.drop(['price', 'ID'], axis=1)
test_id = test.pop('ID')

dum_X = pd.get_dummies(X)
dum_test = pd.get_dummies(test)
# print(dum_test.describe())
dum_test = dum_test.reindex(columns=dum_X.columns, fill_value=0)
# print(dum_X.shape, dum_test.shape)
# print(dum_test.describe())
# print(X.describe())

for col in ['mileage', 'tax','mpg']:
    scaler = StandardScaler()
    dum_X[col] = scaler.fit_transform(dum_X[[col]])
    dum_test[col] = scaler.transform(dum_test[[col]])

X_tr, X_val,y_tr, y_val = train_test_split(dum_X, y, test_size=0.2, random_state=1)
# print(X_tr.shape, X_val.shape, y_tr.shape,y_val.shape)

rf = RandomForestRegressor(max_depth=20, n_estimators=200, random_state=1)
rf.fit(X_tr, y_tr)
rf_pred = rf.predict(X_val)
rf_result = np.sqrt(mean_squared_error(y_val, rf_pred))
# print('rf :', rf_result) # 2601.613607421406

# xgb = XGBRegressor(max_depth=5)
# xgb.fit(X_tr,y_tr)
# xgb_pred = xgb.predict(X_val)
# xgb_result = np.sqrt(mean_squared_error(y_val, xgb_pred))
# print('xgb :', xgb_result) #2768.7534595261614

rf.fit(X_tr, y_tr)
pred = rf.predict(dum_test)
# print(pred[:5])

ans = pd.DataFrame({'ID': test_id, 'price': pred})
ans.to_csv('003000000.csv', index=False)
# print(ans.head())
