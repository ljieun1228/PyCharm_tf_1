"""
데이터 가공 : 리네임 : 전처리 : 프리프로세싱

df_cctv_col
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

df_pop_col
['구별', '인구수', '한국인', '외국인', '고령자']

"""

import pandas as pd
import numpy as np


ctx = '../data/'
df_cctv = pd.read_csv(ctx+'CCTV_in_Seoul.csv')
df_pop = pd.read_excel(ctx+'population_in_Seoul.xls'
                    ,encoding='UTF-8'
                    ,header=2
                    ,usecols='B,D,G,J,N')

df_cctv_col = df_cctv.columns
df_pop_col = df_pop.columns
#head는 위에서 (숫자)만큼 기본은 다섯개다.

df_cctv.rename(columns={df_cctv.columns[0]:'구별'},inplace=True)
# inplace=True 실제 변수의내용을 바꿔라


df_pop.rename(columns={df_pop.columns[0]:'구별'
                         ,df_pop.columns[1]:'인구수'
                         ,df_pop.columns[2]:'한국인'
                         ,df_pop.columns[3]:'외국인'
                         ,df_pop.columns[4]:'고령자'}
                ,inplace=True)

#문제 1] df_cctv 소계를 기준으로 오름차순으로 정렬해라
#print(df_cctv.sort_values(by='소계'))

#문제 2] df_pop 에서 0번행 삭제
"""
df_pop.drop([0], inplace=True)
print(df_pop)
"""

#문제 3] df_pop 에서 구별 기준 중복제거
#print(df_pop.duplicated())
#print(df_pop.drop_duplicated())

#문제 4] df_pop 에서 null 체크 (null이 있는지 여부)
#print(pd.isna(df_pop)) #결측치있으면 T

#문제 5] df_pop 에서 인구수 기준 오름차순 정렬
#print(df_pop.sort_values(by='인구수'))

#문제 6] df_pop 에서 인구수 기준 오름차순 정렬
#print(df_cctv.loc[:,['구별','소계']])


df_pop.drop([0], inplace=True)
df_pop['구별'].unique()
df_pop[df_pop['구별'].isnull()]
df_pop.drop([26], inplace=True)
#연산
df_pop['외국인비율'] = (df_pop['외국인']/df_pop['인구수'])*100
df_pop['고령자비율'] = (df_pop['고령자']/df_pop['인구수'])*100
df_cctv.drop(['2013년도 이전','2014년','2015년','2016년'],1,inplace=True)

df_cctv_pop = pd.merge(df_cctv,df_pop,on='구별')
#print(df_cctv_pop)

#상관계수(Correlation coefficient)
#Corrcoef
'''
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
'''

df_cctv_pop.set_index('구별',inplace=True)

#print(df_cctv_pop)
#np.corrcoef(df_cctv_pop)

cor1 = np.corrcoef(df_pop['외국인비율'],df_cctv_pop['소계'])
cor2 = np.corrcoef(df_pop['고령자비율'],df_cctv_pop['소계'])

#print('외국인비율 상관계수 :\n {} \n 고령자비율 비율 상관계수 :\n {} \n'.format(cor1,cor2))


df_cctv_pop.to_csv(ctx+'cctv_pop.csv')
# 저장하기

