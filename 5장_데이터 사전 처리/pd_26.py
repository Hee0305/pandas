# -*- coding: utf-8 -*-

# 210p 날짜 데이터 분리

import pandas as pd

df = pd.read_csv('stock-data.csv') 

df['new_Date'] = pd.to_datetime(df['Date']) # df에 새로운 열 추가
print(df.head())
print('\n')

#   dt 속성을 이용해 new_Date 열의 연-월-일 정보를 년, 월, 일로 구분
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

#   날짜 데이터 분리
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())

df.set_index('Date_m', inplace=True)
print(df.head())

# 212p 날짜 인덱스 활용
import pandas as pd

df = pd.read_csv('stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date']) #새로운 열에 추가
df.set_index('new_Date', inplace=True) #행 인덱스로 지정

print(df.head())
print('\n')
print(df.index)