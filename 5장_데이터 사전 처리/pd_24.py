# -*- coding: utf-8 -*-

# 198p 정규화 = 변수마다 다른 값의 범위를 동일한 크기 기준으로 나눈 비율로 나타내는 것  0~1

import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락 데이터 행 삭제 
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로 변환

print(df.horsepower.describe()) # horsepower 열의 통계 요약 정보로 최대값(max) 확인
print('\n')

df.horsepower = df.horsepower/abs(df.horsepower.max()) # horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())

print(df.horsepower.describe()) #horsepower 열의 통계 요약 정보로 최대값(max)과 최소(min)확인
print('\n') 

min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x/min_max

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())

# 202p 문자열을 Timestamp로 변환

import pandas as pd

df = pd.read_csv('stock-data.csv')

print(df.head())
print('\n')
print(df.info())

df['new_Date'] = pd.to_datetime(df['Date']) # df에 새로운 열로 추가

print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))

df.set_index('new_Date', inplace=True) # 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정
df.drop('Date', axis=1, inplace=True) # 기존 날짜 열은 삭제

print(df.head())
print('\n')
print(df.info())


