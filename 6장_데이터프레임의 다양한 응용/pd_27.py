# -*- coding: utf-8 -*-

# 218p 시리즈의 원소에 apply() 적용
import seaborn as sns

    # 데이터 로드
titanic = sns.load_dataset('titanic')
    # titanic 데이터셋 중 age, fare 2개의 열을 선택하여 데이터프레임 생성
df = titanic.loc[:,['age','fare']]
df['ten'] = 10
print(df.head())

    # 사용자 함수 정의 
def add_10(n):  # 10을 더하는 함수
    return n + 10
def add_two_obj(a,b):    # 두 객체의 합
    return a + b

print(add_10(10))
print(add_two_obj(10,10))

    # 시리즈 객체에 적용
sr1 = df['age'].apply(add_10)   # n = df['age']의 모든 원소 
print(sr1.head())
print('\n')

    # 시리즈 객체와 숫자에 적용: 2개의 인수(시리즈 + 숫자)
sr2 = df['age'].apply(add_two_obj, b=10)    # a = df['age']의 모든 원소, b=10
print(sr2.head())
print('\n')

    # lambda 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x))  # x=df['age']
print(sr3.head())


# 221p 데이터프레임 원소에 applymap() 적용
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')

    # 사용자 함수 정의
def add_10(n):
    return n+10

    # 데이터프레임에 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)
print(df_map.head())


# 222p 데이터프레임에 apply(axis=0) 적용
import seaborn as sns

    # titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print('\n')

    # 사용자 함수 정의
def missing_value(series):  # 시리즈를 인자로 전달
    return series.isnull()  # 불린 시리즈를 변환

result = df.apply(missing_value, axis=0)
print(result.head())
print('\n')
print(type(result))


# 224p 데이터프레임에 apply(axis=0) 적용

import seaborn as sns

    # titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print('\n')

    # 사용자 함수 정의
def min_max(x): # 최대값 - 최소값
    return x.max() - x.min()    

result = df.apply(min_max, axis=0)
print(result)
print('\n')
print(type(result))


# 225p 데이터프레임에 apply() 적용
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')

def add_two_obj(a,b):    # 두 객체의 합
    return a + b

    # 데이터프레임의 2개 열에 적용
    # x=df, a=df['age'], b=df['ten']
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())

# 226p 데이터프레임에 pipe() 적용
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]

    # 각 열의 NaN 찾기 - 데이터프레임을 전달하면 데이터프레임 반환
def missing_value(x):
    return x.isnull()

    # 각 열의 NaN 개수 반환 - 데이터프레임을 전달하면 시리즈 반환
def missing_count(x):
    return missing_value(x).sum()

    # 데이터프레임의 총 NaN 개수 - 데이터플임을 전달하면 값 변환
def totoal_number_missing(x):
    return missing_count(x).sum()

result_df = df.pipe(missing_value) 
print(result_df.head())
print(type(result_df))

result_series = df.pipe(missing_count)
print(result_series)
print(type(result_series))

result_value = df.pipe(totoal_number_missing)
print(result_value)
print(type(result_value))



