# -*- coding: utf-8 -*-

# 38p 행, 열 바꾸기 (transpose)
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

df = df.transpose() # transpose를 사용하여 df를 전치 한다.
print(df)
print('\n')

df = df.T #transpose 와 같은 역할, df를 전치 한다. 
print(df) 

# 39p 특정 열을 행 인덱스로 지정
import pandas as pd

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

ndf = df.set_index(['이름']) # 특정 column을 데이터프레임의 행 index 로 설정
print(ndf)
print('\n')
ndf2 = ndf.set_index(['음악'])
print(ndf2)
print('\n')
ndf3 = ndf.set_index(['수학', '음악'])
print(ndf3)

