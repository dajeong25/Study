# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:35:45 2023

@author: GD

Perceptron 퍼셉트론 : 인공신경망 ANN

y = x1w1 + x2w2 + b

  x1, x2 : 입력값, 입력층
  y      : 결과값
  w1, w2 : 가중치
  b      : 편향
    
"""

import numpy as np
def AND(x1, x2) :
    x = np.array([x1, x2])  #입력값
    w = np.array([0.5,0.5]) #가중치
    b = -0.8 #편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

for xs in [(0,0), (0,1), (1,0), (1,1)]:
    y = AND(xs[0], xs[1])
    print(xs, "=>", y)
    

'''
tensorflow 설치
conda install tenserflow
install 확인
python
import tensorflow
tensorflow.__version__
'''

# 텐서플로를 이용하여 AND 구현하기
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import mse

data=np.array([[0,0], [0,1], [1,0], [1,1]])
label=np.array([[0],[0],[0],[1]])

# 딥러닝 모델 저장 객체
model = Sequential() 

'''
Dense : 밀집층
    1 : 출력값의 갯수
    input_shape : 입력값의 갯수,
    activation : 활성화 함수
        linear : 선형함수 a==y
        sigmoid : 0~1 사이의 값 변경
        rele : 양수인 경우 선형함수, 음수인 경우 0'''
model.add(Dense(1, input_shape=(2,), activation='linear'))

'''
compile : 가중치를 찾는 방법 설정
    optimizer=SGD() : 경사하강법 알고리즘 설정
    loss=mse : 손실함수, 평균제곱오차
               손실함수값이 적은 경우의 가충지와 편향 구함
    metrics=['acc'] : 평가방법 지정 > acc=정확도
    
좋은 모델이란 ? 손실함수값이 적고, 정확도는 1에 가까운 가중치와 편향 값을 구하는 것'''
model.compile(optimizer=SGD(),loss=mse, metrics=['acc'])

'''
학습하기
data : 학습데이터
label : 정답
epochs=300 : 300번 학습
verbose=0 : 학습과정 상세 출력 생략
verbose=1 : 기본값, 학습과정 상세 출력
verbose=2 : 학습과정 상세 간략출력 '''
model.fit(data,label,epochs=300,verbose=2)

# 평가하기
print(model.get_weights()) #가중치 값과 편향 값 출력
print(model.predict(data)) #예측
print(model.evaluate(data, label)) #평가
