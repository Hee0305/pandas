# -*- coding: utf-8 -*-

# 22p 행 선택
import pandas as pd

exam_data = {'수학' : [90,80,70], '영어':[98,89,95],
             '음악' : [85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('\n')
print(position2)

# 23p 행 선택

label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print('\n')
print(position3)

# 24p 열 선택 

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학'] # '수학'점수데이터만 선택, math1 에 저장
print(math1)
print(type(math1))
print('\n')

english = df.영어 # '영어' 점수데이터만 선택, english 에 저장
print(english)
print(type(english))

# 26p 
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

music_gym = df[['음악','체육']]
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

