import numpy as np
list= [5,4,7,6,2,1]

arr1 = np.array(list)

print(arr1)
print (" Type: " , type(arr1))
print(" Shape: ", arr1.shape)
print(" size: ", arr1.size)
print("DImesnions:" , arr1.ndim)
print(" Data type: ", arr1.dtype)
print("Item_Size:",arr1.itemsize) 
print("total_memory: =", arr1.size * arr1.itemsize,"bytes")
