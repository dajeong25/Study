### 출처 : https://www.datamanim.com/dataset/practice/ex4.html
### 기출 4회 제2유형 ####
import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p2_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p2_test.csv')
pd.set_option('display.max_columns', None)
# print(train.info())
# print(test.info())
# print(train.head())
# print(test.head())
# print(train.describe(include='all'))
# print(test.describe(include='all'))

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
# from sklearn.ensemble import 
print(train.isnull().sum())
print(test.isnull().sum())
