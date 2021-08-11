# -*- coding: utf-8 -*-

# 74p CSV 파일로 저장 (to_csv)
import pandas as pd

data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C","B","B+"],
        'c++' : ["B+","C","C+"]}

df = pd.DataFrame(data)
print(df)
df.set_index('name', inplace=True) # name 열을 인덱스로 지정
print(df)

df.to_csv("./df_sample.csv")

# 75p JSON 파일로 저장 (to_json)
data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C","B","B+"],
        'c++' : ["B+","C","C+"]}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_json("./df_sample.json")

# 77p Excel 파일로 저장
data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C","B","B+"],
        'c++' : ["B+","C","C+"]}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_excel("./df_sample.xlsx")


# 78p ExcelWriter() 활용 
data1 = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "A+", "B"],
        'basic' : ["C","B","B+"],
        'c++' : ["B+","C","C+"]}

data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c2':[7,8,9],
         'c3':[10,11,12],
         'c4':[13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)

writer = pd.ExcelWriter("./df_excelwriter.xlsx") 
df1.to_excel(writer, sheet_name="sheet1") #sheet1 에 저장
df2.to_excel(writer, sheet_name="sheet2") #sheet2 에 저장
writer.save()