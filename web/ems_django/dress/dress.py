# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:09:35 2023

"""
from keras.models import load_model
import matplotlib.pyplot as plt
import cv2
from pathlib import Path


def predict(img_url):
    try:
        basedir = str(Path.cwd())
        src = plt.imread(img_url)
        m = load_model(basedir+'/file/dress/cloths_model1.h5')
    
        image = cv2.resize(src, dsize=(112,112))
        image = image/255 #min-max 정규화
        image = image.reshape((1,) + image.shape) #4차원형태의 이미지로 변경
    
        pred = m.predict(image) #예측
    
        #가장 큰 값 2개를 레이블과 함께 출력
        class_col = ['black', 'blue', 'brown', 'green', 'red', 'white'
                     , 'dress', 'shirt', 'pants', 'shorts', 'shoes']
        prob = zip(class_col, list(pred[0]))
        prob = sorted(list(prob), key=lambda x: x[1], reverse=True)[:2]
    
        return f'{prob[0][0]} : {round(prob[0][1]*100, 2)}%, {prob[1][0]} : {round(prob[1][1]*100, 2)}%'
    except Exception as ex:
        print(ex)
        return "판별할 수 없는 이미지입니다(jpg 파일만 가능)"
        