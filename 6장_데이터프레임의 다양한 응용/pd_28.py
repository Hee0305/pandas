# -*- coding: utf-8 -*-

# 229p 열 순서 바꾸기 
import seaborn as sns

    # titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
print(df, '\n')

columns = list(df.columns.values) # 기존 열 이름
print(columns, '\n')

    # 열 이름을 알파벳 순으로 정렬하기
columns_sorted = sorted(columns) # 알파벳 순으로 정렬
df_sorted = df[columns_sorted]
print(df_sorted, '\n')

columns_reversed = list(reversed(columns))
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

columns_customed = ['pclass','sex','age','survived'] # 열 이름을 사용자가 정의한 임의의 순서로 재배치하
df_customed = df[columns_customed]
print(df_customed)


# 232p 열 분리하기
import pandas as pd

df = pd.read_excel('./주가데이터.xlsx')
print(df.head(),'\n')
print(df.dtypes, '\n')

df['연월일'] = df['연월일'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
dates = df['연월일'].str.split('-')    # 문자열을 split() 메소드로 분리
print(dates.head(), '\n')

    # 분리된 정보를 각각 새로운 열에 담아 df에 추가하기 
df['연'] = dates.str.get(0)  # dates 변수의 원소 리스트의 0번째 인덱스 값
df['월'] = dates.str.get(1)  # dates 변수의 원소 리스트의 1번째 인덱스 값
df['일'] = dates.str.get(2)  # dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head())


# 235p 불린 인덱싱
import seaborn as sns

titanic = sns.load_dataset('titanic')

    # 나이가 10대(10~19) 인 승객만 따로 선택
mask1 = (titanic.age >= 10) & (titanic.age < 20) 
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())

    # 나이가 10세 미만(0~9세)이고 여성인 승객만 따로 선택
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())

    # 나이가 10세 미만(0~9세) 또는 60세 이상인 승객의 age, sex, alone 열만 선택
mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morethan60 = titanic.loc[mask3, ['age','sex','alone']]
print(df_under10_morethan60.head())

