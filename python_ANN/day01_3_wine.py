# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:01:47 2023

@author: GD
"""
### 이진분류 : 분류의 종류가 2종류인 경우 ###
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'
red = pd.read_csv(url+'winequality-red.csv', sep=';')
white = pd.read_csv(url+'winequality-white.csv', sep=';')
print(red.info())   #1599건
print(white.info()) #4898건

red['type'] = 0
white['type'] = 1

print(red.head())
print(white.head())

# wine 데이터 생성
wine = pd.concat([red, white])
print(wine.info()) #6497건
print(wine.min())
print(wine.max())

### 정규화
wine_norm = (wine-wine.min()) / (wine.max() - wine.min())
print(wine_norm)
print(wine_norm.min())
print(wine_norm.max())
print(wine_norm['type'].head())
print(wine_norm['type'].tail())

# wine_norm 데이터 섞어서 wine_shuffle 데이터 생성
# sample(frac=1) : 임의로 표본추출 
    # / frac=1 : 100% >> 전체데이터를 표본추출
wine_shuffle = wine_norm.sample(frac=1)
print(wine_shuffle['type'].head())
print(wine_shuffle['type'].tail())
print(wine_shuffle.info()) #Int64Index: 6497 entries, 617 to 4160

wine_np = wine_shuffle.to_numpy()
print(type(wine_np))
print(wine_np.shape) #(6497, 13)

import numpy as np
train_idx = int(len(wine_np)*0.8) #훈련데이터 개수
print(train_idx) #5197 

# 설명변수(독립변수), 목표변수(종속변수| 정답, 레이블)로 분리
train_x, train_y = wine_np[:train_idx, :-1], wine_np[:train_idx, -1]
print(train_x.shape, train_y.shape) #(5197, 12) (5197,)

# 데스트 데이터 분리
test_x, test_y = wine_np[train_idx:, :-1], wine_np[train_idx:, -1]
print(test_x.shape, test_y.shape)   #(1300, 12) (1300,)

# label을 ont-hot 인코딩
import tensorflow as tf
train_y = tf.keras.utils.to_categorical(train_y, num_classes=2)
test_y = tf.keras.utils.to_categorical(test_y, num_classes=2)
print(train_y, test_y)

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

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(train_x, train_y, epochs=25, batch_size=32, validation_split=0.25)

