# -*- coding: utf-8 -*-

# 148p 회귀선이 있는 산점도 ( regplot() 함수는 서로 다른 2개의 연속 변수 사이의 산점도를 그리고 선형 회귀분석에 대한 회귀선을 나타냄)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic=sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())

sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5)) # figure에 2개의 서브플롯 생성
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# ---- 그래프 그리기 - 선형회귀선 표시    
sns.regplot(x='age',  # x축 변수
            y='fare', # y축 변수
            data=titanic, # 데이터
            ax=ax1) # axe 객체 - 1번째 그래프 

sns.regplot(x='age',  # x축 변수
            y='fare', # y축 변수
            data=titanic, # 데이터
            ax=ax2,  # axe 객체 - 2번째 그래프 
            fit_reg=False,
            color='blue') # 회귀선 미표시

plt.show()

# 149p 히스토그램/커널 밀도 그래프

fig = plt.figure(figsize=(15, 5)) # 그래프 객체 생성(figure에 3개의 서브 플롯 생성) 
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

sns.distplot(titanic['fare'], ax=ax1) # 기본값

sns.distplot(titanic['fare'], hist=False, ax=ax2) # hist=False

sns.distplot(titanic['fare'], kde=False, ax=ax3) # kde=False

ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - ked')
ax3.set_title('titanic fare - hist')

plt.show()


# 151p 히트맵 

table = titanic.pivot_table(index=['sex'], columns=['class'],aggfunc='size')

sns.heatmap(table, # 데이터프레임
            annot=True, fmt='d', # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu', # 컬러 맵
            linewidth=5, # 구분 선
            cbar=False) # 컬러 바 표시 여부

plt.show()