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
import pandas as pd
train_df = pd.read_csv('./clothes_dataset/train.csv')
val_df = pd.read_csv('./clothes_dataset/val.csv')
test_df = pd.read_csv('./clothes_dataset/test.csv')
print(train_df.info())
print(test_df.info())
print(val_df.info())

# 원본이미지 출력
import matplotlib.pyplot as plt
img1 = plt.imread(train_df['image'][0])
print(img1.shape) #(474, 474, 3) green shoes
plt.imshow(img1)
img2 = plt.imread(train_df['image'][1])
print(img2.shape) #(494, 474, 3) brown pants
plt.imshow(img2) 
img3 = plt.imread(train_df['image'][2])
print(img3.shape) #(640, 474, 3) white dress
plt.imshow(img3)
## >> 이미지 크기가 모두 다름 == 분석 불가능

# 1. 이미지 분석을 위해 이미지 크기를 동일하게 설정
# 2. 이미지 제너레이터 이용
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
# 정규화
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

model = Sequential([
    # Conv2D : CNN 관련된 신경망 층
        # input_shape= 학습데이터 크기
        # kernel_size= 특징맵을 위한 커널 크기
        # padding= 출력크기 보정하는 충전재 역할.
            # 'same' : 입력데이터 크기 == 특징맵 크기. 줄어들지 않음
            # 'valid' : 패딩 적용x = 입력 사이즈 보다 줄어듦
    Conv2D(input_shape=(112,112,3), kernel_size=(3,3)
           , filters=32, padding='same', activation='relu')
    , Conv2D(kernel_size=(3,3), filters=64, padding='same', activation='relu')
    , MaxPool2D(pool_size=(2,2))
    , Dropout(rate=0.5) #학습데이터 중 50%는 학습에서 제외
    , Conv2D(kernel_size=(3,3), filters=128, padding='same',activation='relu')
    , Conv2D(kernel_size=(3,3), filters=256, padding='valid',activation='relu')
    , MaxPool2D(pool_size=(2,2)) #(2,2) 사이즈 안에서 가장 큰 값만 가져옴 : input size를 줄임
    , Dropout(rate=0.5)
    , Flatten() #1차원 배열로 펴줌
    , Dense(units=512, activation='relu')
    , Dropout(rate=0.5)
    , Dense(units=256, activation='relu')
    , Dropout(rate=0.5)
    , Dense(units=11, activation='sigmoid') #출력층. 11개의 출력값
    ])
model.summary()
    # Model: "sequential"
    # _________________________________________________________________
    #  Layer (type)                Output Shape              Param #   
    # =================================================================
    #  conv2d_4 (Conv2D)           (None, 112, 112, 32)      896       
                                                                     
    #  conv2d_5 (Conv2D)           (None, 112, 112, 64)      18496     
                                                                     
    #  max_pooling2d_1 (MaxPoolin  (None, 56, 56, 64)        0         
    #  g2D)                                                            
                                                                     
    #  dropout_1 (Dropout)         (None, 56, 56, 64)        0         
                                                                     
    #  conv2d_6 (Conv2D)           (None, 56, 56, 128)       73856     
                                                                     
    #  conv2d_7 (Conv2D)           (None, 54, 54, 256)       295168    
                                                                     
    #  max_pooling2d_2 (MaxPoolin  (None, 27, 27, 256)       0         
    #  g2D)                                                            
                                                                     
    #  dropout_2 (Dropout)         (None, 27, 27, 256)       0         
                                                                     
    #  flatten (Flatten)           (None, 186624)            0         
                                                                     
    #  dense (Dense)               (None, 512)               95552000  
                                                                     
    #  dropout_3 (Dropout)         (None, 512)               0         
                                                                     
    #  dense_1 (Dense)             (None, 256)               131328    
                                                                     
    #  dropout_4 (Dropout)         (None, 256)               0         
                                                                     
    #  dense_2 (Dense)             (None, 11)                2827      
                                                                     
    # =================================================================
    # Total params: 96074571 (366.50 MB)
    # Trainable params: 96074571 (366.50 MB)
    # Non-trainable params: 0 (0.00 Byte)
    # _________________________________________________________________

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

class_col = list(train_df.columns[1:])
print(class_col) 
    #['black', 'blue', 'brown', 'green', 'red', 'white'
    # , 'dress', 'shirt', 'pants', 'shorts', 'shoes']
batch_size=32
train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df   # dataframe 객체
    , directory = None   # 이미지 폴더 지정. 폴더 설정되어 있으므로 설정x
    , x_col = 'image'    # 분석 이미지를 가진 컬럼명
    , y_col = class_col  # 레이블데이터
    , target_size= (112,112)  #생성될 이미지 크기
    , color_mode = 'rgb' # 색상지정. 컬러이미지
    # Invalid class_mode:{'raw', 'categorical', 'input', 'binary', 'sparse', 'multi_output', None}
    , class_mode = 'raw' # 레이블데이터 자료형. 배열로 리턴
    , batch_size = batch_size #한번에 생성되는 이미지 개수
    , shuffle=True, seed=42
    ) #Found 5578 validated image filenames.

# 검증 데이터 설정
val_generator = val_datagen.flow_from_dataframe(
    dataframe = val_df
    , directory = None
    , x_col = 'image'
    , y_col = class_col
    , target_size= (112,112) 
    , color_mode = 'rgb'
    , class_mode = 'raw'
    , batch_size = batch_size
    , shuffle=True
    ) #Found 2391 validated image filenames.

def get_steps(num_samples, batch_size) :
    if(num_samples % batch_size) > 0:
        return (num_samples // batch_size) +1
    else:
        return (num_samples // batch_size)

history5 = model.fit(train_generator
                    , steps_per_epoch=get_steps(len(train_df), batch_size)
                    , validation_data=val_generator
                    , validation_steps=get_steps(len(val_df), batch_size)
                    , epochs=5)
    # Epoch 1/5
    # 175/175 [==============================] - 499s 3s/step - loss: 0.4637 - acc: 0.2426 - val_loss: 0.2911 - val_acc: 0.6750
    # Epoch 2/5
    # 175/175 [==============================] - 481s 3s/step - loss: 0.2626 - acc: 0.5880 - val_loss: 0.1682 - val_acc: 0.7403
    # Epoch 3/5
    # 175/175 [==============================] - 470s 3s/step - loss: 0.1881 - acc: 0.6502 - val_loss: 0.1363 - val_acc: 0.7754
    # Epoch 4/5
    # 175/175 [==============================] - 469s 3s/step - loss: 0.1504 - acc: 0.6655 - val_loss: 0.1109 - val_acc: 0.7210
    # Epoch 5/5
    # 175/175 [==============================] - 462s 3s/step - loss: 0.1283 - acc: 0.6710 - val_loss: 0.1170 - val_acc: 0.7679
    
# 학습데이터 모델 저장
model.save("clothes_model_epo5.h5")
# 결과 그래프 출력
import matplotlib.pyplot as plt
batch = next(train_generator)
image,level = batch[0], batch[1] #32개의 이미지 데이터 리턴
print(image.shape, level.shape) 
    #(32, 112, 112, 3) (32, 11)
  #32개의 이미지 데이터 #32개의 이미지 레이블 저장
plt.imshow(image[-3])
print(level[-3]) #[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

# 학습 결과 그래프로 출력
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
# history.history['loss']: 손실함수, 값이 낮을 수록 성능이 좋다
plt.plot(history5.history['loss'], '-b', label='loss')
plt.plot(history5.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('Epoch')
plt.legend()
plt.subplot(1,2,2)
# history.history['acc'] : 정확도, 값이 1에 가까울수록 성능이 좋다
plt.plot(history5.history['acc'], 'g-', label='acc')
plt.plot(history5.history['val_acc'], 'k--', label='val_acc')
plt.xlabel('Epoch')
plt.legend();
# >> 검증데이터 결과가 더 좋다. 즉, 과적합이 일어나지 않음.

# 테스트 데이터 예측
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

preds = model.predict(test_generator, steps=32)
print(preds[0])
    # [9.5730251e-01 2.5757025e-03 4.9016736e-02 1.1073100e-02 4.7665781e-05
    #  4.3393295e-05 2.1216879e-04 1.3561816e-03 9.9119025e-01 1.6323458e-02
    #  2.9466138e-03]
print(preds.shape) # (1024, 11)

off = 0
do_preds = preds[off:off+8]
for i, pred in enumerate(do_preds):
    plt.subplot(2,4,i+1) #2행4열1번째, ...
    prob = zip(class_col, list(pred))
    # 예측된 확률값의 내림차순 정렬
    # 확률값이 높은 2개의 값만 prob 데이터 저장
    prob = sorted(list(prob), key=lambda x: x[1], reverse=True)[:2]
    image = plt.imread(test_df['image'][i+off]) #테스트 데이터의 원본이미지
    plt.imshow(image) #이미지 출력
    plt.title(f'{prob[0][0]} : {round(prob[0][1]*100, 2)}%\n \
{prob[1][0]} : {round(prob[1][1]*100,2)}%')
    plt.tight_layout()
plt.show()
