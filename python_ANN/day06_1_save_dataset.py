# -*- coding: utf-8 -*-
"""
### 캐글데이터 - 이미지 분석

https://www.kaggle.com/trolukovich/apparel-images-dataset 이미지 다운
-> clothes_dataset 폴더에 저장

1. 다중레이블 데이터
      빨강 파랑 신발 드레스
       1    0    1    0
       1    0    0    1
  - 활성화함수 : sigmoid
  - 손실함수 : binary_crossentropy

2. 다중클래스 데이터 : 다중 컬럼 데이터 
      ex) 숫자 맞추기
      빨강 파랑 신발 드레스
       1    0    0    0
       0    0    0    1
       0    1    0    0
  - 활성화함수 : softmax
  - 손실함수 : categorical_crossentropy

3. 이진클래스 데이터 : 이중컬럼데이터
      남자 여자
       0    1
       1    0
  - 활성화함수 : sigmoid
  - 손실함수 : binary_crossentropy
"""
# 1) 데이터 전처리 : 레이블 지정
import numpy as np
import pandas as pd
import tensorflow as tf
import glob

# glob.glob : 파일의 목록을 읽어서 리스트 리턴함수
# recursive=True : 하위 폴더까지 검색
all_data = np.array(glob.glob("./clothes_dataset/*/*.jpg", recursive=True))
len(all_data)
print(all_data[:5])

# 다중레이블을 위함 함수
def check_cc(color, clothes):
    labels = np.zeros(11,)
    if color=='black' : labels[0]=1
    elif color== 'blue' : labels[1]=1
    elif color== 'brown' : labels[2]=1
    elif color== 'green' : labels[3]=1
    elif color== 'red' : labels[4]=1
    elif color== 'white' : labels[5]=1
    else: pass
    if clothes== 'dress' : labels[6]=1
    elif clothes== 'shirt' : labels[7]=1
    elif clothes== 'pants' : labels[8]=1
    elif clothes== 'shorts' : labels[9]=1
    elif clothes== 'shoes' : labels[10]=1
    else: pass
    return labels

all_labels = np.empty((all_data.shape[0], 11))
print(all_data.shape[0], all_data.shape) #11385 (11385,)

for i,data in enumerate(all_data):
    # print(i, data) #0 ./clothes_dataset\black_dress\0097960878307e559459d98c9f9eaeeea0db1f94.jpg
    color_n_clothes = all_data[i].split('\\')[1].split('_')
    # print(color_n_clothes) #['black', 'dress']
    color = color_n_clothes[0]
    clothes = color_n_clothes[1]
    labels = check_cc(color, clothes)
    # print(labels) #[1. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
    all_labels[i] = labels
print(all_labels[:10])
print(all_labels[-10:])

# 데이터분리 : train, test, velidation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(all_data,all_labels,shuffle=True,random_state=99,test_size=0.3)
print(X_train.shape, X_test.shape) #(7969,) (3416,)
print(y_train.shape, y_test.shape) #(7969, 11) (3416, 11)

x_train, x_val, y_train, y_val = \
    train_test_split(X_train,y_train,test_size=0.3,shuffle=True,random_state=99)
print(x_train.shape, x_val.shape) #(5578,) (2391,)
print(y_train.shape, y_val.shape) #(5578, 11) (2391, 11)

# df 생성
train_df = pd.DataFrame({
    "image":x_train, 'black':y_train[:,0],'blue':y_train[:,1]
    , "brown":y_train[:,2], 'green':y_train[:,3], 'red':y_train[:,4]
    , 'white':y_train[:,5], 'dress':y_train[:,6], 'shirt':y_train[:,7]
    , 'pants':y_train[:,8], 'shorts':y_train[:,9], 'shoes':y_train[:,10]
    })
print(train_df.info())
# print(train_df.head())
val_df = pd.DataFrame({
    "image":x_val, 'black':y_val[:,0],'blue':y_val[:,1]
    , "brown":y_val[:,2], 'green':y_val[:,3], 'red':y_val[:,4]
    , 'white':y_val[:,5], 'dress':y_val[:,6], 'shirt':y_val[:,7]
    , 'pants':y_val[:,8], 'shorts':y_val[:,9], 'shoes':y_val[:,10]
    })
print(val_df.info())

test_df = pd.DataFrame({
    "image":X_test, 'black':y_test[:,0],'blue':y_test[:,1]
    , "brown":y_test[:,2], 'green':y_test[:,3], 'red':y_test[:,4]
    , 'white':y_test[:,5], 'dress':y_test[:,6], 'shirt':y_test[:,7]
    , 'pants':y_test[:,8], 'shorts':y_test[:,9], 'shoes':y_test[:,10]
    })
print(test_df.info())

# csv로 저장
train_df.to_csv('./clothes_dataset/train.csv', index=None)
val_df.to_csv('./clothes_dataset/val.csv', index=None)
test_df.to_csv('./clothes_dataset/test.csv', index=None)
