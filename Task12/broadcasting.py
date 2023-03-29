import numpy as np
arr = np.arange(5)
print(arr)
print(arr*4) #multiplying scalar with array


#demean
arr2 = np.random.randn(4, 3)
arr2.mean(0)
demeaned = arr2 - arr2.mean(0)
print(demeaned)

print(demeaned.mean(0))



row_means = arr2.mean(1)
print(row_means.shape)
print(row_means.reshape((4, 1)))
demeaned = arr2 - row_means.reshape((4, 1))
print(demeaned.mean(1))

arr2 - arr2.mean(1).reshape((4, 1))

arr3 = np.zeros((4, 4))
arr_3d = arr3[:, np.newaxis, :]
print(arr_3d.shape)

arr_1d = np.random.normal(size=3)
arr_1d[:, np.newaxis]

print(arr_1d[np.newaxis, :])


#setting array values by broadcasting
arr = np.zeros((4, 3))
arr[:] = 5
print(arr)

col = np.array([1.28, -0.42, 0.44, 1.6])
arr[:] = col[:, np.newaxis]
arr[:2] = [[-1.37], [0.509]]
print(arr)