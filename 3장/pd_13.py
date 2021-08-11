# -*- coding: utf-8 -*-
# 90p 각 열 데이터 개수 

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.count()) # 각 열이 가지고 있는 원소 개수 확인
print('\n')
print(type(df.count()))


# 91p 각 열의 고유값 개수

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
print(type(unique_values))


# 92p 평균값(mean)

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())


# 93p 중간값(median())

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.median())
print('\n')
print(df['mpg'].median())


# 94p 최대값(max())
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.max())
print('\n')
print(df['mpg'].max())


# 95p 최소값(min())
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.min())
print('\n')
print(df['mpg'].min())


# 96p 표준편차(std())
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.std())
print('\n')
print(df['mpg'].std())


# 97p 상관계수(corr())
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())



