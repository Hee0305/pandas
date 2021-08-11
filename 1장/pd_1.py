# -*- coding: utf-8 -*-

# 13p
import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data)

print(type(df)) # df의 자료형 출력
print('\n')
print(df)

# 14p
import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서','예은'],
                  columns=['나이', '성별', '학교'])

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

# 15p
import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['학생1','학생2'],
                  columns=['연령', '남녀', '소속'])

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

# 16p // rename (행, 열 이름 변경)
import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index=['준서','예은'],
                  columns=['나이', '성별', '학교'])

print(df)
print('\n')

df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True) #inplace=True // 원본 객체 변경
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)

print(df)


# 17p // drop (행, 열 삭제)
import pandas as pd

exam_data = {'수학' : [90,80,70], '영어':[98,89,95],
             '음악' : [85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:] # df2 = df 복사 
df2.drop('우현', inplace=True)
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현','인아'], axis=0, inplace=True) # axis=0 행 삭제 
print(df3)

#20p // 열 삭제 

df4 = df[:]
df4.drop('수학', axis=1, inplace=True) #axis=1 열 삭제 
print(df4)
print('\n')

df4 = df[:]
df4.drop(['영어','음악'], axis=1, inplace=True) #axis=1 열 삭제 
print(df4)

#21p // 행 선택 

import pandas as pd

exam_data = {'수학' : [90,80,70], '영어':[98,89,95],
             '음악' : [85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)



