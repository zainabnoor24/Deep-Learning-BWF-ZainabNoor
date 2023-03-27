import numpy as np
arr=np.arange(100000)
lst=list(range(100000))


#2d array

array2d=np.random.randn(2,3)
print(array2d)

x=array2d * 10
print(x)

#3d array
array3d=np.zeros((2,3,4))

#arithmatic operations
array1=np.array([[1,2,3,4,5],[1,2,4,1,3]])
print(array1)
print("multiplcation",array1*array1)
print("sum",array1+array1)
print("subtraction",array1-array1)
print("division",array1/array1)



# Boolean operations
print(array1 > 2)   
print(array1 < 3)   
print((array1 > 5) & (array1 < 1))  
print((array1 > 2) | (array1 < 4))   
print(~(array1 > 2))   