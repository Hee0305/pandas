# -*- coding: utf-8 -*-

# 192p 데이터 구간 분할 / 구간을 나누기 위해서는 경계값을 구해야함 = Numpy 의 histogram() 사용 

import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None) # 데이터 불러오기

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name'] # 열이름 지정

df['horsepower'].replace('?', np.nan, inplace=True) # ? -> np.nan
df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락 데이터 행 삭제
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로 변환

count, bin_dividers = np.histogram(df['horsepower'], bins=3) # np.histogram 함수로 3개의 bin으로 구분할 경계값의 리스트 구하기 
print(bin_dividers)

bin_names=['저출력', '보통출력', '고출력'] # 3개의 bin에 이름 지정

    # --- pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'], # 데이터 배열
                      bins=bin_dividers, # 경계값 리스트
                      labels=bin_names, # bin 이름
                      include_lowest=True) # 첫 경계값 포함

print(df[['horsepower', 'hp_bin']].head(15)) # horsepower 열, hp_bin 열의 첫 15행 출력


# 194p 더미 변수 = 0 또는 1로 표현되는 수 / 범주형 데이터를 컴퓨터가 인식가능하게 변환한다 =  one-hot-encoding
# 판다스 get_dummies() 함수사용

count, bin_dividers = np.histogram(df['horsepower'], bins=3) # 3개의 bin으로 구분할 경계값의 리스트 구하기 
print(count)
bin_names=['저출력', '보통출력', '고출력'] # 3개의 bin에 이름 저장

df['hp_bin'] = pd.cut(x=df['horsepower'], #데이터 배열
                      bins=bin_dividers, # 경계값 리스트
                      labels=bin_names, # bin 이름
                      include_lowest=True) # 첫 경계값 포함

horsepower_dummies = pd.get_dummies(df['hp_bin']) # hp_bin 열의 범주형 데이터를 더미 변수로 변환
print(horsepower_dummies.head(15))


# 196p 원핫인코딩 / sklearn 활용
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder() # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder() # one hot encoder 생성

# 1. label encoder로 문자열 범주 -> 숫자형 범주 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15)) 
print(onehot_labeled)
print(type(onehot_labeled))

# 2. 2차원 행렬로 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) 
print(onehot_reshaped)
print(type(onehot_reshaped)) 

# 3. 희소 행렬로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))