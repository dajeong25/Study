# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:36:17 2023
"""
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression

def fun_predict(day, p_we):
    if p_we == "avg_temp":
        pr_y = "평균기온(℃)"
    elif p_we == "max_temp":
        pr_y = "최고기온(℃)"
    elif p_we == "min_temp":
        pr_y = "최저기온(℃)"
    else: pass
    weather_url = "D:/emspy/python_web/emsjango/file/weather/seoul.csv"
    df = pd.read_csv(weather_url)
    
    # 년도 컬럼 생성
    df["년도"] = df["날짜"].apply(lambda x : x[:4]).copy()
    df0721 = df[df["날짜"].apply(lambda x : x[5:])==day].copy()
    
    # 결측값 제거
    df0721.dropna(subset=["평균기온(℃)", "최고기온(℃)", "최저기온(℃)"], axis=0, inplace=True)
    
    # 모델 생성
    model = LinearRegression()
    X = df0721[["년도"]]
    y = df0721[pr_y]
    model.fit(X.values, y.values)
    result = model.predict([[2023]])
    return result


# if __name__ == "__main__":
#     weather_url = "D:/emspy/python_web/emsjango/file/weather/seoul.csv"
#     df = pd.read_csv(weather_url)
#     # print(df.info())
#     # print(df.head())
    
#     ##### 2023.07.21 날짜 예측하기 #####
    
#     # 년도 컬럼 생성
#     df["년도"] = df["날짜"].apply(lambda x : x[:4])
#     df0721 = df[df["날짜"].apply(lambda x : x[5:])=='07-21']
#     print(df0721.info())
    
#     # 결측값 제거
#     df0721.dropna(subset=["평균기온(℃)", "최고기온(℃)", "최저기온(℃)"],
#                   axis=0, inplace=True)
#     print(df0721.info())
    
#     # 모델 생성
#     model = LinearRegression()
#     X = df0721[["년도"]]
#     y = df0721["최고기온(℃)"]
#     model.fit(X.values, y.values)
    
#     result = model.predict([[2023]])    
#     print(result)
