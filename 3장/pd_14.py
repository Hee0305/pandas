# -*- coding: utf-8 -*-
import pandas as pd

# 99p 선 그래프 그리기 (.plot())

df = pd.read_excel('./남북한발전전력량.xlsx')
print(df)

df_ns = df.iloc[[0, 5], 3:] # 남, 북한 발전량 합계 데이터만 추출


df_ns.index = ['South','North'] # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경
print(df_ns.head())

print('\n')

df_ns.plot()

tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()


# 102p  막대 그래프 그리기 ( plot(kind='bar') )

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:] # 남, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South','North'] # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경

# ---- 행, 열 전치하여 막대 그래프 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot(kind='bar')


# 103p 히스토그램 ( plot(kind='hist') ) 
df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:] # 남, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South','North'] # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경

tdf_ns = df_ns.T
tdf_ns.plot(kind='hist')


# 104p 산점도 (scatter)
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df.plot(x='weight', y='mpg', kind='scatter')


# 105p 박스 플롯 (box) = 특정 변수의 데이터 분포와 분산 정도에 대한 정보 제공
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df[['mpg','cylinders']].plot(kind='box')

