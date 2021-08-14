# -*- coding: utf-8 -*-

# 186p 단위 환산

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
print(df.head(3))
print('\n')

mpg_to_kpl = 1.60934/3.78541 # mpg(mile per gallon) -> kpl(kilometer per liter)로 변환

df['kpl'] = df['mpg']*mpg_to_kpl # mpg 옆에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
print(df.head(3))
print('\n')

df['kpl'] = df['kpl'].round(2) # kpl 열을 소수점 아래 둘째자리에서 반올림
print(df.head(3))


# 188p 자료형 변환

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.dtypes) # or df.info()
print('\n')

print(df['horsepower'].unique()) # horsepower 열의 고유값 확인
print('\n')

    # --- 누락데이터 ? 삭제
import numpy as np
df['horsepower'].replace('?', np.nan, inplace=True) # ? -> np.nan 으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락 데이터 행 삭제
df['horsepower'] = df['horsepower'].astype('float') # 문자열 -> 실수형 변환

print(df['horsepower'].dtypes)

print(df['origin'].unique()) # origin 열의 고유값 확인

df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True) # 정수형-> 문자열 변환

print(df['origin'].unique())
print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('category') # 문자열 -> 범주형(category) 변환
print(df['origin'].dtypes) 

df['origin'] = df['origin'].astype('str') # 범주형 -> 문자열(str) 변환
print(df['origin'].dtypes)

print(df['model year'].sample(3)) # model year 열의 정수형 -> 범주형
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))