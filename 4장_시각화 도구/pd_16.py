# -*- coding: utf-8 -*-

# 121p 화면 분할해서 여러개의 그래프 그리기
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)
df = df.fillna(method='ffill') # 누락값(nan)을 앞 데이터로 채움
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') # 서울에서 다른 지역으로 이동한 데이터만 추출
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)


sr_one = df_seoul.loc['경기도']

fig = plt.figure(figsize=(10,10)) # figure에 2개의 subplot 생성
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(sr_one, 'o', markersize=10) # axe 객체에 plot 함수로 그래프 출력 
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울->경기')
ax2.legend(loc='best')

ax1.set_ylim(50000,800000) # y축 범위 지정 (최소값, 최대값)
ax2.set_ylim(50000,800000) # y축 범위 지정 (최소값, 최대값)

ax1.set_xticklabels(sr_one.index, rotation=75) # 축 눈금 라벨 지정 및 75도 회전
ax2.set_xticklabels(sr_one.index, rotation=75)

plt.show()