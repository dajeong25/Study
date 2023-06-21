# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
X_test = pd.read_csv("data/X_test.csv")
X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")

# 사용자 코딩
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# print(X_test.info())
# print(X_train.info())
# print(y_train.info())

# 전처리
trian_id = X_train['cust_id']
test_id = X_test['cust_id']
X_train.drop('cust_id', axis=1, inplace=True)
X_test.drop('cust_id', axis=1, inplace=True)
X_train['환불금액'] = X_train['환불금액'].fillna(0)
X_test['환불금액'] = X_test['환불금액'].fillna(0)

# 수치형 스케일 변환
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
scaler = MinMaxScaler()
for i in ['총구매액', '최대구매액','내점일수', '환불금액']:
	X_train[i] = scaler.fit_transform(X_train[[i]])
	X_test[i] = scaler.transform(X_test[[i]])
# print(X_train.describe())

# 범주형 전처리
# print(len(X_train['주구매상품'].unique()))
# print(len(X_train['주구매지점'].unique()))
encoder = LabelEncoder()
for i in ['주구매상품', '주구매지점'] :
	X_train[i] = encoder.fit_transform(X_train[i])
	X_test[i] = encoder.transform(X_test[i])
# print(X_train.describe())

# 분류모델 > 남자일 확률
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=1)
model.fit(X_train, y_train['gender'])
rf_score = model.score(X_train, y_train['gender'])
pred = model.predict_proba(X_val)
print(rf_score) #0.865

# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
pd.DataFrame({'cust_id': test_id, 'gender': pred}).to_csv('006000000.csv', index=False)
