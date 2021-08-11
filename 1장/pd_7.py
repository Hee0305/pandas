# -*- coding: utf-8 -*-

# 45p 열 기준 정렬
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print('\n')

ndf = df.sort_values(by='c1', ascending=False) # c1 열을 기준으로 내림차순 정렬
print(ndf) 

# 46p 시리즈를 숫자로 나누기 

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))


# 47p 시리즈 사칙 연산
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})

print(student1)
print('\n')
print(student2)
print('\n')

addition = student1 + student2 # 덧셈
subtraction = student1 - student2 # 뺄셈
multiplication = student1 * student2 # 곱셈
division = student1 / student2 # 나눗셈
print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

# 49p  Nan 값이 있는 시리즈 연산
import numpy as np
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1)
print('\n')
print(student2)
print('\n')

addition = student1 + student2 # 덧셈
subtraction = student1 - student2 # 뺄셈
multiplication = student1 * student2 # 곱셈
division = student1 / student2 # 나눗셈
print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)



