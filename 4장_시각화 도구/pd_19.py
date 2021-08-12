# -*- coding: utf-8 -*-

# 155p 박스 플롯/바이올린 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) # 박스 플롯 - 기본값

sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) # 박스 플롯 - hue 변수 추가

sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) # 바이올린 그래프 - 기본값

sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) # 바이올린 그래프 - 기본값

plt.show()

# 157p 조인트 그래프 = 기본으로 산점도 + x-y축에 각 변수에 대한 히스토그램을 동시에 보여준다.

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

j1 = sns.jointplot(x='fare', y='age', data=titanic) # 조인트 그래프 - 산점도(기본값)

j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic) # 조인트 그래프 - 회귀선

j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic) # 조인트 그래프 - 육각 그래프

j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic) # 조인트 그래프 - 커널 밀집 그래프

j1.fig.suptitle('titanic fare - scatter', size=15)
j2.fig.suptitle('titanic fare - req', size=15)
j3.fig.suptitle('titanic fare - hex', size=15)
j4.fig.suptitle('titanic fare - kde', size=15)

plt.show()

# 159p 조건에 맞게 화면 분할

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid') # 스타일 테마 설정

g=sns.FacetGrid(data=titanic, col='who', row='survived') # 조건에 따라 그리드 나누기

g = g.map(plt.hist, 'age')


