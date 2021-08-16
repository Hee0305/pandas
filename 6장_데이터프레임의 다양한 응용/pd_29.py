# -*- coding: utf-8 -*-

# 237p isin() 필터링
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

    # IPthon 디스플레이 설정 변경 - 출력할 최대 열의 개수
pd.set_option('display.max_columns', 10)

    # 함께 탑승한 형제 또는 배우자의 수가 3,4,5 인 승객만 따로 추출 - 불린 인덱싱
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())

    # isin() 메소드 활용하여 동일한 조건으로 추출
isin_filter = titanic['sibsp'].isin([3,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())


# 240p 데이터 프레임 연결 (concatenate)
import pandas as pd

df1 = pd.DataFrame({'a': ['a0','a1','a2','a3'],
                    'b': ['b0','b1','b2','b3'],
                    'c': ['c0','c1','c2','c3']},
                    index=[0,1,2,3])

df2 = pd.DataFrame({'a': ['a2','a3','a4','a5'],
                    'b': ['b2','b3','b4','b5'],
                    'c': ['c2','c3','c4','c5'],
                    'd': ['d2','d3','d4','d5']},
                    index=[2,3,4,5])

print(df1)
print(df2)

    # 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기
result1 = pd.concat([df1,df2])
print(result1,'\n')

    # ignore_index=True 옵션 설정하기 -> 정수형 위치 인덱스가 새롭게 설정된다 (0~7 범위)
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2, '\n')

    # axis=1 옵션 -> 좌우 열 방향으로 연결
result3 = pd.concat([df1, df2], axis=1)
print(result3, '\n')

    # join=inner 옵션 -> 행 인덱스의 교집합을 기준으로 사용 ( 양쪽 다 존재하는 데이터만 반환)
result3_in = pd.concat([df1, df2],axis=1, join='inner')
print(result3_in,'\n')

    # 데이터 프레임과 시리즈 연결
sr1 = pd.Series(['e0','e1','e2','e3'], name='e')
sr2 = pd.Series(['f0','f1','f2'], name='f', index=[3,4,5])
sr3 = pd.Series(['g0','g1','g2','g3'], name='g')
    # df1과 sr1을 좌우 열 방향으로 연결하기 
result4 = pd.concat([df1, sr1], axis=1)
print(result4)

result5 = pd.concat([df2, sr2], axis=1, sort=True)
print(result5)

    # sr1과 sr3을 좌우 열 방향으로 연결하기 
result6 = pd.concat([sr1,sr3], axis=1)
print(result6, '\n')
result7 = pd.concat([sr1,sr3], axis=0)
print(result7, '\n') 

