import pandas as pd

ctx = '../data/'
csv = ctx+'CCTV_in_Seoul.csv'
xls = ctx+'population_in_Seoul.xls'

cctv_data = pd.read_csv(csv)
pop_data = pd.read_excel(xls)

print(pop_data.head(10))
print(cctv_data.head(10))
#head는 위에서 (숫자)만큼 기본은 다섯개다.