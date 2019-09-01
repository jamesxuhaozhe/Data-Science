# coding:utf-8
from sklearn import preprocessing
import numpy as np

x = np.array([[0., -3., 1.],
             [3., 1., 2.],
             [0., 1., -1.]])
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)

print minmax_x

scaled_x = preprocessing.scale(x)
print scaled_x

j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x / (10**j)
print scaled_x