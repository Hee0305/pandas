# -*- coding: utf-8 -*-

# 205p Timestamp -> Period 변환
import pandas as pd

dates = ['2019-01-01', '2020-03-01', '2021-06-01'] # 날짜 형식의 문자열로 구성되는 리스트 정의

ts_dates = pd.to_datetime(dates) # 문자열의 배열(시리즈 객체) -> Timestamp 변환
print(ts_dates)
print('\n')

#    Timestamp -> Period(기간) 변환
pr_day = ts_dates.to_period(freq='D') # D = 1일의 기간
print(pr_day) 
pr_month = ts_dates.to_period(freq='M') # M = 1개월의 기간
print(pr_month)
pr_year = ts_dates.to_period(freq='A') # A = 1년의 기간
print(pr_year)


# 206p Timestamp 배열 만들기 
import pandas as pd

ts_ms = pd.date_range(start='2019-01-01', # 날짜 범위 시작
                      end=None, # 날짜 범위 끝
                      periods=6, # 생성할 Timestamp 개수
                      freq='MS', # 시간 간격(MS: 월의 시작일)
                      tz='Asia/Seoul') # 시간대(timezone)
print(ts_ms)

ts_me = pd.date_range('2019-01-01', periods=6,
                      freq='M', # 시간 간격 (M: 월의 마지막 날)
                      tz='Asia/Seoul')  # 시간대(timezone)
print(ts_ms)

# 208p Period 배열 만들기 

import pandas as pd

pr_m = pd.period_range(start='2019-01-01',
                     end=None,
                     periods=3,
                     freq='M')
print(pr_m)

#   period 배열 만들기 - 1시간 길이
pr_h = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='H')
print(pr_h)
print('\n')

#   period 배열 만들기 - 2시간 길이
pr_2h = pd.period_range(start='2019-01-01',
                       end=None,
                       periods=3,
                       freq='2H')
print(pr_2h)
