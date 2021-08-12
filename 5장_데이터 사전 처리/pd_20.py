# -*- coding: utf-8 -*-

import seaborn as sns

df = sns.load_dataset('titanic')
print(df)
print('\n')


nan_deck = df['deck'].value_counts(dropna=False) # value_counts를 이용한 누락데이터 확인 
print(nan_deck)

    # isnull() : 누락 데이터면 True, 유효한 데이터는 False 반환
    # notnull() : 누락 데이터면 False, 유효한 데이터는 True 반환

print(df.head().isnull()) # isnull() 메소드로 누락 데이터 찾기 

print(df.head().notnull()) # notnull() 메소드로 누적 데이터 찾기

print(df.head().isnull().sum(axis=0)) # deck 에만 3개의 누락데이터 확인가능

# 176p 누락 데이터 제거 

df = sns.load_dataset('titanic')

missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts() # 각 열의 NaN 개수 파악
    try:
        print(col, ': ', missing_count[True]) # NaN 값이 있으면 개수 출력
    except: 
        print(col, ': ', 0) # NaN 값이 없으면 0개 출력
        
df_thresh = df.dropna(axis=1, thresh=500) # NaN값이 500개 이상인 열을 모두 삭제 - deck열 (891개 중 688개의 NaN값)
print(df_thresh.columns)

df_age = df.dropna(subset=['age'], how='any', axis=0) # age 열에 나이 데이터가 없는 모든 행 삭제 
print(len(df_age))


# 178p 누락 데이터 치환 

df = sns.load_dataset('titanic')

print(df['age'].head(10)) # age 열의 첫 10개 데이터 출력 / 5행에 NaN값
print('\n')

mean_age = df['age'].mean(axis=0) # age 열의 평균 계산 (NaN값 제외)
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))


# 180p 가장 많이 나타내는 값으로 바꾸기

df = sns.load_dataset('titanic')

print(df['embark_town'][825:830]) #embark_town 열의 829행의 NaN 데이터 출력
print('\n')

most_freq = df['embark_town'].value_counts(dropna=True).idxmax() # embark_town 열의 NaN 값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
print(most_freq)
print('\n')

df['embark_town'].fillna(most_freq, inplace=True)

print(df['embark_town'][825:830])
