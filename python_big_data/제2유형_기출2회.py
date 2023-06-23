### 출처 : https://www.kaggle.com/code/agileteam/tutorial-t2-2-python/notebook
### # 2회 기출 유형 2번 ####
import pandas as pd
df = pd.read_csv('data/Train.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(df, test_size=0.2, random_state=2023)
y_train = X_train[['ID', 'Reached.on.Time_Y.N']]
X_train = X_train.iloc[:, :-1]
y_test = X_test[['ID', 'Reached.on.Time_Y.N']]
X_test = X_test.iloc[:, :-1]

# 사용자 코딩
# 제공된 3개 데이터 (y_test데이터 활용X)
# print(X_train.shape, X_test.shape, y_train.shape)
# print(X_train.describe())

X_train_id = X_train.pop('ID')
X_test_id = X_test.pop('ID')

# 데이터 전처리
# print(X_train.isnull().sum(), X_test.isnull().sum())
# print(X_train.head())
# object : ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
z = X_train[['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']].nunique()
# print(z)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance']:
    X_train[col] = encoder.fit_transform(X_train[col])
    X_test[col] = encoder.transform(X_test[col])

temp = pd.get_dummies(X_train['Gender'])
X_train = pd.concat([X_train, temp], join='outer', axis=1)
X_train.drop('Gender', axis=1, inplace=True)
# print(X_train.head())

temp2 = pd.get_dummies(X_test['Gender'])
X_test = pd.concat([X_test, temp2], axis=1, join='outer')
X_test.drop('Gender', axis=1, inplace=True)
# print(X_test.head())

# 모델 및 평가
from sklearn.ensemble import RandomForestClassifier
# from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
# from sklearn.metrics import roc_auc_score
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train['Reached.on.Time_Y.N'], test_size=0.2, random_state=2021)

rf = RandomForestClassifier(max_depth=9, n_estimators=100, random_state=2023)
# xgb = XGBClassifier(eval_metric='mlogloss')
rf.fit(X_tr, y_tr)
# xgb.fit(X_tr, y_tr)
rf_pred = rf.predict_proba(X_val)
# xgb_pred = xgb.predict_proba(X_val)
# print('rf:', roc_auc_score(y_val, rf_pred[:,1]))
# print('xgb:', roc_auc_score(y_val, xgb_pred[:,1]))

# 답안제출
model = RandomForestClassifier(max_depth=9, n_estimators=100, random_state=2023)
model.fit(X_train, y_train['Reached.on.Time_Y.N'])
pred = model.predict_proba(X_test)

pd.DataFrame({'cust_id': X_test_id, 'Reached.on.Time_Y.N': pred[:,1]}).to_csv('003000000.csv', index=False)
# print(ans.head())
