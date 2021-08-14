# -*- coding: utf-8 -*-

# 181p 누락데이터 이웃하고 있는 값으로 바꾸기

import seaborn as sns

df=sns.load_dataset('titanic')

print(df['embark_town'][825:830])
print('\n')

df['embark_town'].fillna(method='ffill', inplace=True) # 열의 NaN값 바로 앞에 있는 828행의 값으로 변경
print(df['embark_town'][825:830])


# 182p 중복 데이터 확인 (duplicated()) / duplicate = 복제하다

import pandas as pd

df=pd.DataFrame({'c1':['a','a','b','a','b'],
                 'c2':[1,1,1,2,2],
                 'c3':[1,1,2,2,2]})
print(df)
print('\n')

df_dup = df.duplicated() # 데이터프레임 전체 행 데이터 중에서 중복값 찾기 / 중복 = True , 중복x = False 반환
print(df_dup)
print('\n')

col_dup = df['c2'].duplicated() # 특정 열 데이터에서 중복값 찾기 ( c2에서 1과 2가 처음나타난 0,3 인덱스는 제외하고 True를 반환함)
print(col_dup)

# 184p 중복 데이터 제거 (drop_duplicates())

df=pd.DataFrame({'c1':['a','a','b','a','b'],
                 'c2':[1,1,1,2,2],
                 'c3':[1,1,2,2,2]})

print(df)
print('\n')

df2 = df.drop_duplicates() # 중복 행 제거 
print(df2)
print('\n')

# 185p 중복 데이터 제거 (dropo_duplicates(subset)) = subset옵션에 열 삽입

df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)