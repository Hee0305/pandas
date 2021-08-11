# -*- coding: utf-8 -*-

# 41p 행 인덱스 재배열 (reindex) = 행 인덱스를 새로운 "배열" 로 재지정 가능 

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]} # 딕셔너리 정의

df = pd.DataFrame(dict_data, index=['r0','r1','r2']) # 딕셔너리 -> 데이터프레임 으로 변환, 인덱스를 r0,r1,r2로 지정
print(df)
print('\n')

new_index = ['r0','r1','r2','r3','r4']
#print(type(new_index))
ndf = df.reindex(new_index)
print(ndf)

print('\n')

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0) # Nan값을 0으로 
print(ndf2)


# 42p 행 인데스 초기화 
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2']) # 인덱스를 r0,r1,r2 로 지정
print(df)
print('\n')

ndf=df.reset_index() # 행 인덱스를 정수형으로 초기화
print(ndf)

# 43p 행 인덱스를 기준으로 데이터프레임 정렬 (sort)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
#dict_data = {'c0':['a','b'], 'c1':['c','d'], 'c2':['e','f'], 'c3':['g','h']}
df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
#df = pd.DataFrame(dict_data, index=['r0','r1']) # 문자도 됨 ㅋ
print(df)
print('\n')

ndf = df.sort_index(ascending=False) # ascending = 오름차순의
print(ndf)
print('\n')

print(ndf.value_counts())

