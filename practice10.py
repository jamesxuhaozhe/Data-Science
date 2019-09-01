import pandas as pd
from pandas import Series, DataFrame

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

print df1
print df2

df2 = df2.drop(columns=['Chinese'])

df2 = df2.drop(index=['ZhangFei'])

print df2

df2.rename(columns={'English': 'Yinyu'}, inplace=True)

print df2

df2 = df2.drop_duplicates()


