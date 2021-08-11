# -*- coding: utf-8 -*-
# 60p csv 파일읽기

# 라이브러리 불러오기 
import pandas as pd

# 파일 경로
file_path = './read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('함수를 데이터프레임 변환\n')

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('header=None 옵션\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('index_col=None 옵션\n')

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('index_col="c0" 옵션')

