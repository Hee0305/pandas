# -*- coding: utf-8 -*-

# 339p DBSCAN (Density-Based Spatial Clustering of Applications with Noise) = 데이터가 위치한 공간 밀집도를 기준으로 클러스터를 구분
import pandas as pd
import folium

# 1. 데이터 준비/기본 설정
file_path = './2016_middle_shcool_graduates_report.xlsx'
df = pd.read_excel(file_path, header=0)

    # Ipython Console 디스플레이 옵션 설정하기 
pd.set_option('display.width', None) # 출력 화면의 너비
pd.set_option('display.max_rows', 100) # 출력할 행의 개수 한도
pd.set_option('display.max_columns', 10) # 출력할 열의 개수 한도
pd.set_option('display.max_colwidth', 20) # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) # 유니코드 사용 너비 조정

    # 열 이름 배열 출력
print(df.columns.values)

# 2. 데이터 탐색

    # 데이터 살펴보기
print(df.head())
print('\n')

    # 데이터 자료형 확인
print(df.info())
print('\n')

    # 데이터 통계 요약 정보 확인
print(df.describe())
print('\n')

    # 지도에 위치 표시
mschool_map = folium.Map(location=[37,55,126.98], tiles='Stamen Terrain', zoom_start=12)

    # 중학교 위치 정보를 CircleMarker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=5, # 원의 반지름
                        color='brown', # 원의 둘레 색상
                        fill=True,
                        fill_color='coral', # 원을 채우는 색
                        fill_opacity=0.7, # 투명도
                        popup=name).add_to(mschool_map)
                        
    # 지도를 html 파일로 저장하기
mschool_map.save('./seoul_mschool_location.html')
    