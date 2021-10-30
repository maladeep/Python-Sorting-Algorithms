import time
import numpy as np
def insertionSort(arr):  
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and arr[j] > key : 
                arr[j+1] = arr[j] 
                j -= 1
#                 print("iteration : (",i,j,")")
        arr[j+1] = key
size1=100000
a = np.random.randint(low=1, high=1000000, size=size1)
a = a.tolist()
start = time.time()
insertionSort(a)
end = time.time()
print("Time taken for size of ", size1, " is",end-start)
