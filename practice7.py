import numpy as np

a = np.array([1, 2, 3, 4])

wts = np.array([1, 2, 3, 4])

print np.average(a)

print np.average(a, weights=wts)

print np.std(a)

print np.var(a)