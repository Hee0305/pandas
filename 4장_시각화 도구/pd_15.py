# -*- coding: utf-8 -*-

# 108p 선 그래프 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)#.fillna(0)
#print(df)

# --- print(df.isna().sum()) // Nan 값 갯수 세기

df = df.fillna(method='ffill') # 누락값(nan)을 앞 데이터로 채움

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') # 서울에서 다른 지역으로 이동한 데이터만 추출

df_seoul = df[mask]
#print(df_seoul)
df_seoul = df_seoul.drop(['전출지별'], axis=1)
#print(df_seoul)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
#print(df_seoul)
df_seoul.set_index('전입지', inplace=True)
#print(df_seoul)

sr_one = df_seoul.loc['경기도']
#print(sr_one)

#plt.plot(sr_one.index, sr_one.values)
plt.plot(sr_one)  # == plt.plot(sr_one.index, sr_one.values) 


# 112p 차트 제목, 축 이름 추가

sr_one = df_seoul.loc['경기도'] #서울에서 경기도로 이동한 인구 데이터 값만 선택

plt.plot(sr_one) # plot

plt.title('서울->경기 인구 이동') # 타이틀 명 지정

plt.xlabel('기간') # x축 이름 추가 
plt.ylabel('이동 인구수') # y축 이름 추가

plt.show() # 변경사항 저장 및 출력

# 113p Matplotlib 한글 폰트 오류 해결

from matplotlib import font_manager, rc
font_path = "./malgun.ttf" # 폰트파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# 115p 그래프 꾸미기 

sr_one = df_seoul.loc['경기도']

plt.style.use('ggplot') #ggplot 외에 다양한 스타일이 있다 118p 참고 

plt.figure(figsize=(14,5)) # 그림사이즈 지정 (가로 14인치, 세로 5인치)

plt.xticks(rotation='vertical') # x축 눈금 라벨 회전

plt.plot(sr_one, marker='o') # sr_one 출력

plt.title('서울->경기 인구 이동') # 차트 이름
plt.xlabel('기간') # x축 이름
plt.ylabel('이동 인구수') # y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best') # 범례 표시 

plt.show()
