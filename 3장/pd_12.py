# -*- coding: utf-8 -*-

# 85p 데이터 살펴보기 

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')
print(df.tail())

# 86p 데이터프레임 크기 (shape)

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

#print(df.head())
#print('\n')
#print(df.tail())
print(df.shape)



# 87p 데이터프레임의 기본정보 (info())

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.info())


# 88p 데이터 살펴보기 

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.dtypes)
print('\n')
print(df.mpg.dtpyes)


# 89p 데이터프레임의 기술 통계 정보 요약 (describe())

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.describe())
print('\n')
print(df.describe(include='all'))
