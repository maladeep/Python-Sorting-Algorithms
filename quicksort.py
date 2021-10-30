import numpy as np
import time

def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)
        
        
a = np.random.randint(low=1, high=10000, size=100)
a = a.tolist()
print("initial:",a)
start = time.time()
quick_sort(a,0,len(a)-1)
end = time.time()
print("Time taken is",end-start)