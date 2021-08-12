# -*- coding: utf-8 -*-

# 152p  범주형 데이터의 산점도 

import matplotlib.pyplot as plt
import seaborn as sns


titanic = sns.load_dataset('titanic') # seaborn 제공 데이터셋 가져오기 

sns.set_style('whitegrid') # 스타일 테마 설정

fig = plt.figure(figsize=(15,5)) # 그래프 객체 생성, 2개의 서브 플롯 생성
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

sns.stripplot(x="class", # x축 변수
              y="age", # y축 변수 
              data=titanic, # 데이터셋 = 데이터프레임
              ax=ax1) # axe 객체 - 1번째

sns.stripplot(x="class", # x축 변수
              y="age", # y축 변수 
              data=titanic, # 데이터셋 = 데이터프레임
              ax=ax2) # axe 객체 - 2번째

ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()

# 153p 막대그래프

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

sns.barplot(x='sex', y='survived', data=titanic, ax=ax1) # x축 y축에 변수 할당

sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2) # x축 y축에 변수 할당하고 hue 옵션을 추가

sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3) # x축 y축에 변수 할당하고 hue 옵션을 추가하여 누적출력

ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')

plt.show()

# 154p 빈도 그래프

fig = plt.figure(figsize=(15,5))
ax4 = fig.add_subplot(1,3,1)
ax5 = fig.add_subplot(1,3,2)
ax6 = fig.add_subplot(1,3,3)

sns.countplot(x='class', palette='Set1', data=titanic, ax=ax4) # 기본값

sns.countplot(x='class',hue='who',palette='Set2',data=titanic, ax=ax5) # hue옵션에 'who'추가

sns.countplot(x='class',hue='who',palette='Set2',dodge=False,data=titanic, ax=ax6) # dodge=False 옵션 추가 ( 축 방향으로 분리x)

ax4.set_title('titanic class')
ax5.set_title('titanic class - who')
ax6.set_title('titanic class - who(stacked)')

plt.show()




