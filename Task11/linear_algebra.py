import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

print(x)
print(y)

x.dot(y)

np.dot(x,y)
np.dot(x, np.ones(3))


a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
print("array is:",a)
print("median is:",np.median(a))
print("mean is:",np.mean(a))
print("average is:",np.average(a))
print("standard deviation:",np.std(a))
print ("variance:",np.var([1,2,3,4]))

