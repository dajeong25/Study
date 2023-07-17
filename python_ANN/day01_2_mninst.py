### mnist 데이터를 이용하여 숫자 학습하기 ###
# 이미지 : 0~255 값 > 0==검정, FF==흰색
from tensorflow.keras.datasets.mnist import load_data
(X_train, y_train), (X_test, y_test) = load_data(path='mnist.npz')
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# 이미지 출력
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
for idx in range(3):
    img = X_train[idx, :] #0번이미지, img:2차원배열(28,28)
    label = y_train[idx]  #0번이미지, 정답. 숫자
    plt.figure()
    plt.imshow(img) #이미지값으로 이미지 출력
    plt.title('%d-th data, label is %d' % (idx,label),fontsize=13)

# 검증데이터 생성 : 학습 중간에 평가를 위한 데이터
from sklearn.model_selection import train_test_split
# random_state=777 : 검증데이터의 일관성
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=777)
print(X_train.shape, X_val.shape) #훈련(42000, 28, 28) / 검증(18000, 28, 28)
print(X_test.shape) #(10000, 28, 28)
 
# 레이블 전처리 : ont-hot 인코딩
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

### 데이터 정규화
# 1. MinMax normalization : X = (x-min) / (max-min) 
# 2. Robust normalization : X = (x-중간값) / (3사분위값 - 1사분위값)
### 데이터 표준화
# Standard normalization : X = (x-평균값) / 표준편차
### 현재데이터 : 최소값 0 / 최대값 255
X_train = (X_train.reshape(42000, 28*28))/255
X_val = (X_val.reshape(18000, 28*28))/255
X_test = (X_test.reshape(10000, 28*28))/255
print(X_train.shape, X_val.shape, X_test.shape) #(42000, 784) (18000, 784) (10000, 784) 3차원에서 2차원으로
X_train[0]

# model 구성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential() #모델 생성

# 1층 : 
#     64 : 출력노드 개수
#     activation='relu' : 활성화함수
#     input_shape=(784,) : 입력노드 개수
model.add(Dense(64, activation='relu', input_shape=(784,))) #28*28 배열

# 2층 :
#     32 : 출력노드 개수
#     activation='relu' : 활성화함수
#     입력값 개수 : 1층의 출력노드 개수
model.add(Dense(32, activation='relu'))

# 3층 :
#     10 : 출력노드 개수 >> 결과값
#     activation='softmax' : 활성화함수
#     입력값 개수 : 2층의 출력노드 개수, 32개
model.add(Dense(10, activation='softmax'))
model.summary()
# Param #  : 가중치, 편향의 개수
# 1층 : 784 + 1(편향) * 64 = 785*64 = 50240
# 2층 : 64 + 1(편향) * 32 = 2080
# 3층 : 32 + 1(편향) * 10 = 330
# Total params: 52650 : 50240+2080+330 = 52650  

# optimizer='adam' : 경사하강법 알고리즘
# loss='categorical_crossentropy' : 손실함수
    # mse : 평균제곱오차
    # categorical_crossentropy : 다중분류에서 사용(출력값이 여러개인 경우, 10개의 출력값임)
    # 다중분류 == 반드시 one-hot 인코딩 되어야 함.
        # 활성화함수 : 일반적으로 softmax와 사용됨 >> 반드시는 아님.
    # binary_crossentropy : 이진분류에서 사용되는 손실함수(출력값이 2개인 경우, 생존자ox)
        # 활성화함수 : 보통 sigmode와 사용됨. 반드시는 아님
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

# epochs=30 : 30번 학습
# batch_size=127 : 데이터를 127개로 분리. 기본값: 32
#     42000/127 = 330.70866141732284 >> 331이 데이터를 학습
# validation_data=(X_val,y_val) : 검증데이터 설정
# history : 학습과정의 저장하고 있는데이터
history = model.fit(X_train,y_train, epochs=30, batch_size=127, validation_data=(X_val,y_val))
print(history.history["loss"]) #학습데이터 손실함수값
print(len(history.history["loss"])) #30
print(history.history["val_loss"]) #검증데이터 손실함수값
print(len(history.history["val_loss"])) #30
# 정확도 히스토리
print(history.history['acc'])
print(history.history['val_acc'])

### 결과 시각화
his_dict = history.history #dict형
# 손실함수 그래프
loss = his_dict['loss']
val_loss = his_dict['val_loss']
epochs=range(1,len(loss)+1)      # 1~30
fig = plt.figure(figsize=(10,5)) # 가로: 10, 세로: 5 크기
ax1 = fig.add_subplot(1,2,1)     # 1행2열 1번째 그래프
ax1.plot(epochs, loss, color='blue', label='train_loss')
ax1.plot(epochs, val_loss, color='orange', label='val_loss')
ax1.set_title('train and val loss')
ax1.set_xlabel('epochs')
ax1.set_ylabel('loss')
ax1.legend()
# 정확도 그래프
acc=his_dict['acc']
val_acc=his_dict['val_acc']
ax2=fig.add_subplot(1,2,2)  # 1행2열 2번째 그래프
ax2.plot(epochs, acc, color='blue', label='acc')
ax2.plot(epochs, val_acc, color='orange', label='val_acc')
ax2.set_title('train and val accuracy')
ax2.set_xlabel('epochs')
ax2.set_ylabel('accuracy')
ax2.legend()
plt.show()
# >> 과적합 현상 발생 == 훈련을 너무 많이함. 훈련을 해도 검증 데이터 평가지수 개선x == 모델 검증 필요

### 모델 평가
model.evaluate(X_test, y_test) #[0.12494505941867828, 0.9725000262260437]
### 예측하기
results = model.predict(X_test)
print(results[:10])
print(np.argmax(results, axis=1)) # 각 행 배열 중 가장 큰 값의 인덱스 가져옴
print(len(np.argmax(results, axis=1))) #10000
y_test
print(np.argmax(y_test, axis=1))

### 이미지 출력
arg_results = np.argmax(results, axis=1)
plt.figure(figsize=(6,6))
for idx in range(16):
    plt.subplot(4,4, idx+1)
    plt.axis('off')
    plt.imshow(X_test[idx].reshape(28,28))
    plt.title('Pred:%d, lab:%d' % (arg_results[idx], np.argmax(y_test[idx], axis=-1)), fontsize=13)
plt.tight_layout()
plt.show()
 
### 혼동 행렬 조회
from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(np.argmax(y_test, axis=-1), np.argmax(results, axis=-1))
print(cm)
# 전체 평가 지표
cr = classification_report(np.argmax(y_test, axis=-1), np.argmax(results, axis=-1))
print(cr)

### heatmap으로 출력
import seaborn as sns
plt.figure(figsize=(7,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('preducted', fontsize=13)
plt.yticks(rotation=360)
plt.ylabel('true label', fontsize=13);
