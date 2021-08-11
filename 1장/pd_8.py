# -*- coding: utf-8 -*-

# 51p 연산 메소드 사용 -시리즈 연산
import pandas as pd
import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1)
print('\n')
print(student2)
print('\n')

# ---- 누락데이터 NaN 대신 0 을 채워줌 = fill_value=0
sr_add = student1.add(student2, fill_value=0) # 덧셈
sr_sub = student1.sub(student2, fill_value=0) # 뺄셈
sr_mul = student1.mul(student2, fill_value=0) # 곱셈
sr_div = student1.div(student2, fill_value=0) # 나눗셈

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


# 53p 데이터프레임에 숫자 더하기 
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition = df + 10 # 데이터 프레임에 +10
print(addition.head())
print('\n')
print(type(addition))


# 54p 데이터프레임끼리 더하기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition = df + 10 
print(addition.head())
print('\n')
print(type(addition))

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))

