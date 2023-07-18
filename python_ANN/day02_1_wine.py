# -*- coding: utf-8 -*-

### 이진분류 : 분류의 종류가 2종류인 경우 ###
import pandas as pd
import numpy as np
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'
red = pd.read_csv(url+'winequality-red.csv', sep=';')
white = pd.read_csv(url+'winequality-white.csv', sep=';')
# print(red.info())   #1599건
# print(white.info()) #4898건

red['type'] = 0
white['type'] = 1

# print(red.head())
# print(white.head())

# wine 데이터 생성
wine = pd.concat([red, white])
# print(wine.info()) #6497건
# print(wine.min())
# print(wine.max())

### 정규화
wine_norm = (wine-wine.min()) / (wine.max() - wine.min())
# print(wine_norm)
# print(wine_norm.min())
# print(wine_norm.max())
# print(wine_norm['type'].head())
# print(wine_norm['type'].tail())

# wine_norm 데이터 섞어서 wine_shuffle 데이터 생성
# sample(frac=1) : 임의로 표본추출 
    # / frac=1 : 100% >> 전체데이터를 표본추출
wine_shuffle = wine_norm.sample(frac=1)
# print(wine_shuffle['type'].head())
# print(wine_shuffle['type'].tail())
# print(wine_shuffle.info()) #Int64Index: 6497 entries, 617 to 4160

wine_np = wine_shuffle.to_numpy()
# print(type(wine_np))
# print(wine_np.shape) #(6497, 13)

train_idx = int(len(wine_np)*0.8) #훈련데이터 개수
# print(train_idx) #5197 

# 설명변수(독립변수), 목표변수(종속변수| 정답, 레이블)로 분리
train_x, train_y = wine_np[:train_idx, :-1], wine_np[:train_idx, -1]
# print(train_x.shape, train_y.shape) #(5197, 12) (5197,)

# 데스트 데이터 분리
test_x, test_y = wine_np[train_idx:, :-1], wine_np[train_idx:, -1]
# print(test_x.shape, test_y.shape)   #(1300, 12) (1300,)

# label을 ont-hot 인코딩
import tensorflow as tf
train_y = tf.keras.utils.to_categorical(train_y, num_classes=2)
test_y = tf.keras.utils.to_categorical(test_y, num_classes=2)
# print(train_y, test_y)

# 모델생성
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model = Sequential([
    Dense(units=48, activation='relu', input_shape=(12,)),
    Dense(units=24, activation='relu'),
    Dense(units=12, activation='relu'),
    Dense(units=2, activation='sigmoid')  #이중분류
    ])
print(model.summary())

# binary_crossentropy
    # : 이진분류에서 사용되는 손실함수
    #  레이블을 onthot 인코딩 필요
    #  활성화 함수는 보통 sigmoid 사용

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#학습을 안 한 상태에서 평가
pre = model.evaluate(test_x, test_y)
# print(pre) #[0.6657425165176392, 0.7699999809265137]

# validation_split=0.25 : 훈련데이터 중 25%를 검증데이터로 사용
history = model.fit(train_x, train_y, epochs=25, batch_size=32, validation_split=0.25)

# 결과 시각화
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5)) # 가로: 10, 세로: 5 크기
plt.subplot(1,2,1)     # 1행2열 1번째 그래프
plt.plot(history.history['loss'], 'b-', label='train_loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.subplot(1,2,2)  # 1행2열 2번째 그래프
plt.plot(history.history['accuracy'], 'b-', label='accuracy')
plt.plot(history.history['val_accuracy'], 'r--', label='val_accuracy')
plt.xlabel('epochs')
plt.ylim(0.7, 1) #y축 값 범위 표시
plt.legend()
plt.show()
####과적합 없음

#평가하기
result = model.evaluate(test_x, test_y)
# print(result) #[0.07446818053722382, 0.986923098564148]

#예측데이터
pred = model.predict(test_x)
arg_pred = np.argmax(pred, axis=-1)
arg_test = np.argmax(test_y, axis=-1)
# print(pred[:10])
# print(arg_pred[:10])
# print(test_y[:10])
# print(arg_test[:10])

#혼동행렬
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
cm = confusion_matrix(arg_pred, arg_test)
# print(cm)  # [[300  11]  예측
             #  [  6 983]] 실제
             #   ~N   ~P
cm2 = confusion_matrix(arg_test, arg_pred)
print(cm2)  #[[300   6]  ~N
            # [ 11 983]] ~P
            # 예측 실제
import seaborn as sns
plt.figure(figsize=(7,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('preducted', fontsize=13)
plt.xticks(range(2), ['red','white'], rotation=45)
plt.yticks(range(2), ['red','white'], rotation=0)
plt.ylabel('true label', fontsize=13)
plt.tight_layout();

print('정확도: %.3f' % accuracy_score(arg_pred,arg_test)) # 정확도: 0.987
print('정밀도:%.3f' % precision_score(arg_pred,arg_test)) # 정밀도:0.989
print('재현율:%.3f' % recall_score(arg_pred,arg_test))    # 재현율:0.994
print('f1 score:%.3f' % f1_score(arg_pred,arg_test))     # f1 score:0.991
# 실제와 같은 예측 : TN, TP
# 실제와 다른 예측 : FN, FP
# 정확도 : 전체 중에 정확하게 예측한 비율
(300+983) / (300+11+6+983) #0.9869230769230769
# 정밀도 : 긍정으로 예측(TP+FP) 것 중에 실제 긍정(TP)인 것
983/(983+11) #0.9889336016096579
# 재현율 : 실제(TP+FN) 긍정 데이터 중에 긍정으로 예측(TP)한 것
983/(6+983) #0.993933265925177
# f1-score : 조화평균 = (정밀도*재현율) / (정밀도+재현율)
