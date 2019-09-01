import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print np.percentile(a, 50)
print np.percentile(a, 50, axis=0)
print np.percentile(a, 50, axis=1)


print np.median(a)
print np.median(a, axis=0)
print np.median(a, axis=1)

print np.mean(a)
print np.mean(a, axis=0)
print np.mean(a, axis=1)
