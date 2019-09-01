import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print a
print np.ptp(a)
print np.ptp(a, 0)
print np.ptp(a, 1)
