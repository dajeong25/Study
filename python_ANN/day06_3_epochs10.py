# -*- coding: utf-8 -*-
"""
### 캐글데이터 - 이미지 분석

https://www.kaggle.com/trolukovich/apparel-images-dataset 이미지 다운
-> clothes_dataset 폴더에 저장

다중레이블 데이터
      빨강 파랑 신발 드레스
       1    0    1    0
       1    0    0    1
  - 활성화함수 : sigmoid
  - 손실함수 : binary_crossentropy
"""
# kernel restrart : 초기화 >> csv 파일로 작업
import numpy as np
import pandas as pd
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
## 기존의 5번만 학습한 모델
test_df = pd.read_csv('./clothes_dataset/test.csv')
m = load_model('./clothes_dataset/clothes_model_epo5.h5')

# 테스트 데이터 예측
batch_size=32
test_datagen = ImageDataGenerator(rescale=1./255) #정규화
test_generator = test_datagen.flow_from_dataframe(
    dataframe = test_df, directory = None
    , x_col = 'image' #test_df image 컬럼을 예측 이미지 설정
    , y_col = None    #정답 설정 안 함
    , target_size = (112,112) #예측을위한 이미지 크기
    , color_mode = 'rgb' #컬럼 이미지
    , class_mode = None  #컬럼명 사용안 함
    , batch_size=batch_size #32개씩 이미지 생성
    , shuffle=False
    ) #Found 3416 validated image filenames.

preds = m.predict(test_generator, steps=32)

off = 8
do_preds = preds[off:off+8]
class_col = list(test_df.columns[1:])
for i, pred in enumerate(do_preds):
    plt.subplot(2,4,i+1) #2행4열1번째, ...
    prob = zip(class_col, list(pred))
    # 예측된 확률값의 내림차순 정렬
    # 확률값이 높은 2개의 값만 prob 데이터 저장
    prob = sorted(list(prob), key=lambda x: x[1], reverse=True)[:2]
    print(i, prob)
    image = plt.imread(test_df['image'][i+off]) #테스트 데이터의 원본이미지
    plt.imshow(image) #이미지 출력
    plt.title(f'{prob[0][0]} : {round(prob[0][1]*100, 2)}%\n \
{prob[1][0]} : {round(prob[1][1]*100,2)}%')
    plt.tight_layout()
plt.show()


## 강사님께 받은 전체 모델
m = load_model('./clothes_dataset/cloths_model1.h5')
m.summary()
    # Model: "sequential"
    # _________________________________________________________________
    #  Layer (type)                Output Shape              Param #   
    # =================================================================
    #  conv2d (Conv2D)             (None, 112, 112, 32)      896       
                                                                     
    #  conv2d_1 (Conv2D)           (None, 112, 112, 64)      18496     
                                                                     
    #  max_pooling2d (MaxPooling2  (None, 56, 56, 64)        0         
    #  D)                                                              
                                                                     
    #  dropout (Dropout)           (None, 56, 56, 64)        0         
                                                                     
    #  conv2d_2 (Conv2D)           (None, 56, 56, 128)       73856     
                                                                     
    #  conv2d_3 (Conv2D)           (None, 54, 54, 256)       295168    
                                                                     
    #  max_pooling2d_1 (MaxPoolin  (None, 27, 27, 256)       0         
    #  g2D)                                                            
                                                                     
    #  dropout_1 (Dropout)         (None, 27, 27, 256)       0         
                                                                     
    #  flatten (Flatten)           (None, 186624)            0         
                                                                     
    #  dense (Dense)               (None, 512)               95552000  
                                                                     
    #  dropout_2 (Dropout)         (None, 512)               0         
                                                                     
    #  dense_1 (Dense)             (None, 256)               131328    
                                                                     
    #  dropout_3 (Dropout)         (None, 256)               0         
                                                                     
    #  dense_2 (Dense)             (None, 11)                2827      
                                                                     
    # =================================================================
    # Total params: 96074571 (366.50 MB)
    # Trainable params: 96074571 (366.50 MB)
    # Non-trainable params: 0 (0.00 Byte)
    # _________________________________________________________________

preds = m.predict(test_generator, steps=32)

off = 0
do_preds = preds[off:off+8]
class_col = list(test_df.columns[1:])
for i, pred in enumerate(do_preds):
    plt.subplot(2,4,i+1) #2행4열1번째, ...
    prob = zip(class_col, list(pred))
    # 예측된 확률값의 내림차순 정렬
    # 확률값이 높은 2개의 값만 prob 데이터 저장
    prob = sorted(list(prob), key=lambda x: x[1], reverse=True)[:2]
    # print(i, prob)
    image = plt.imread(test_df['image'][i+off]) #테스트 데이터의 원본이미지
    plt.imshow(image) #이미지 출력
    plt.title(f'{prob[0][0]} : {round(prob[0][1]*100, 2)}%\n \
{prob[1][0]} : {round(prob[1][1]*100,2)}%')
    plt.tight_layout()
plt.show()

test_df.loc[2,]
do_preds[2]

#####################################
import cv2
src = plt.imread("./clothes_dataset/black_pants/1c84c7697dfab421ba85972c6e8a3cf4847a0bfd.jpg")
print(src.shape) #(474, 474, 3)

#이미지크기 조정
image = cv2.resize(src, dsize=(112,112))
print(image.shape)
plt.imshow(image)
#data 정규화
image = image/255 #min-max 정규화
plt.imshow(image)
#4차원형태의 이미지로 변경
image = image.reshape((1,) + image.shape)
print(image.shape) #(1, 112, 112, 3) 

pred = m.predict(image)
print(pred)

#가장 큰 값 2개를 레이블과 함께 출력
prob = zip(class_col, list(pred[0]))
prob = sorted(list(prob), key=lambda x: x[1], reverse=True)[:2]
print(prob) #[('pants', 1.0), ('blue', 0.9781056)]

plt.figure()
plt.imshow(src) #이미지 출력
plt.title(f'{prob[0][0]} : {round(prob[0][1]*100, 2)}%,\n \
{prob[1][0]} : {round(prob[1][1]*100, 2)}%')
plt.tight_layout()

