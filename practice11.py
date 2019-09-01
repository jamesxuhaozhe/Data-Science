import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

df2['Chinese'].astype('str')

df2['Chinese'].astype(np.int64)

df2['Chinese'].astype('str')

df2['Chinese'] = df2['Chinese'].map(str.strip)

df2['Chinese'] = df2['Chinese'].map(str.lstrip)

df2['Chinese'] = df2['Chinese'].map(str.rstrip)

