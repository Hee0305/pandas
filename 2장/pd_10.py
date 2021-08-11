# -*- coding: utf-8 -*-

# 63p Excel 파일 읽기
import pandas as pd

df1 = pd.read_excel('./남북한발전전력량.xlsx') # header=0 (default 옵션)
df2 = pd.read_excel('./남북한발전전력량.xlsx', header=None) # header=None 옵션

print(df1)
print('\n')
print(df2)


# 64p JSON 파일 읽기

df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)


# 67p 웹에서 표 정보 읽기 

url ='./sample.html'

tables = pd.read_html(url)

print("표 의 개수: ",len(tables)) # 표 의 개수 확인
print('\n')

for i in range(len(tables)): # tables 리스트의 원소를 iteration(반복)하면서 각각 화면 출력
    print("tables[%s]" %i)
    print(tables[i])
    print('\n')
    
df = tables[1]

df.set_index(['name'], inplace=True)
print(df)

