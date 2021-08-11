# -*- coding: utf-8 -*-

# 31p 열 추가
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

df['국어'] = 80 # 열 추가 
print(df)



# 32p 행 추가  ~ 34p
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

df.loc[3] = 0 # 행 추가 - 같은 원소 값 입력
print(df)
print('\n')

df.loc[4] = ['동규', 90, 80, 70, 60] # 행 추가 - 원소 값 여러 개의 배열 입력
print(df)
print('\n')

df.loc['행5'] = df.loc[3] # 행 추가 - 기존 행 복사 
print(df)

# 35p 원소 값 변경
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

df.set_index('이름', inplace=True) # '이름' 열을 새로운 인덱스로 지정
print(df)
print('\n')

df.iloc[0][3] = 80 # index 0 columns 3 서준의 체육점수 변경
print(df)
print('\n')


df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준','체육'] = 100
print(df)

df.loc['서준', ['음악', '체육']] = 50 # 서준의 음악과 체육을 50으로 바꿔줌
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100,50 # 서준의 음악과 체육을 100 과 50 으로 동시에 바꿔줌
print(df)

