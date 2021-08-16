# -*- coding: utf-8 -*-

# 245p 데이터프레임 병합 (merge) 
import pandas as pd

    #IPython 디스플레이 설정 변경
pd.set_option('display.max_columns', 10) # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20) # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) # 유니코드 사용 너비 조정

    # 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')

print(df1)
print('\n')
print(df2)
print('\n')

    # 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1, df2)
print(merge_inner)


    # 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1, df2, how='outer', on='id') # 'id'열을 키로 병합, how='outer' 는 id열을 기준으로 어느 한쪽에만 속하더라도 포함
print(merge_outer)

    # 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name') # left_on, right_on 옵션 사용하여 좌우 df에 각각다르게 키를 지정 할 수 있다.
print(merge_left)

    # 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right)

    # 불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head())
print('\n')

value = pd.merge(price, df2)
print(value)

# 252p 데이터프레임 병합 (join)

    #IPython 디스플레이 설정 변경
pd.set_option('display.max_columns', 10) # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20) # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) # 유니코드 사용 너비 조정

    # 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx', index_col='id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id')

    # 데이터프레임 결합(join)
df3 = df1.join(df2)
print(df3)

    # 데이터프레임 결합(join) - 교집합
df4 = df1.join(df2, how='inner')
print(df4)