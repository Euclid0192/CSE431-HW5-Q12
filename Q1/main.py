def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)
    

def merge(arr1, arr2):
    i, j = 0, 0
    res = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else: 
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    
    return res 

def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    
    return arr 

import random 
import timeit
random.seed(2910)

merge_sort_runtime = []
insertion_sort_runtime = []
for i in range(1, 2001):
    arr = [random.randint(1, 10**6) for _ in range(i)]
    
    start_time = timeit.default_timer()
    # Merge sort
    merge_sort_arr = mergeSort(arr)
    merge_runtime = timeit.default_timer() - start_time
    merge_sort_runtime.append(merge_runtime)
    # Insertion sort
    start_time = timeit.default_timer()
    insertion_sort_arr = insertionSort(arr)
    insertion_runtime = timeit.default_timer() - start_time
    insertion_sort_runtime.append(insertion_runtime)
    
    # print(merge_sort_arr)
    # print(insertion_sort_arr)

# print("Merge sort\n", merge_sort_runtime)
# print("Insertion sort\n", insertion_sort_runtime)

import matplotlib.pyplot as plt
import numpy as np

x = np.array([i for i in range(1, 2001)])
y1 = np.array(merge_sort_runtime)
y2 = np.array(insertion_sort_runtime)

plt.plot(x, y1, label="Merge Sort Runtime")
plt.plot(x, y2, label="Insertion Sort Runtime")
plt.xlabel("Array size")
plt.ylabel("Runtime in seconds")
plt.legend()
plt.show()