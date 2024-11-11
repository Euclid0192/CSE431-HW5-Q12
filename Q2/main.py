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

def timSort(arr, k):
    if len(arr) <= k:
        return insertionSort(arr)

    mid = len(arr) // 2
    left = timSort(arr[:mid], k)
    right = timSort(arr[mid:], k)
    
    return merge(left, right)

import random 
import timeit
random.seed(2910)

merge_sort_runtime = []
insertion_sort_runtime = []
tim_sort_runtime = dict()
for i in range(1, 2001):
    arr = [random.randint(1, 10**6) for _ in range(i)]
    # Merge sort
    start_time = timeit.default_timer()
    copy_arr = arr[:]
    merge_sort_arr = mergeSort(copy_arr)
    merge_runtime = timeit.default_timer() - start_time
    merge_sort_runtime.append(merge_runtime * 10**6)
    # Insertion sort
    start_time = timeit.default_timer()
    copy_arr = arr[:]
    insertion_sort_arr = insertionSort(copy_arr)
    insertion_runtime = timeit.default_timer() - start_time
    insertion_sort_runtime.append(insertion_runtime * 10**6)

    for k in range(1, 100):
        # Tim sort
        tim_sort_runtime[k] = tim_sort_runtime.get(k, [])
        start_time = timeit.default_timer()
        copy_arr = arr[:]
        tim_sort_arr = timSort(copy_arr, k)
        tim_runtime = timeit.default_timer() - start_time
        tim_sort_runtime[k].append(tim_runtime * 10**6)
    
    # print(merge_sort_arr)
    # print(insertion_sort_arr)

# print("Merge sort\n", merge_sort_runtime)
# print("Insertion sort\n", insertion_sort_runtime)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([i for i in range(1, 2001)])
y1 = np.array(merge_sort_runtime)
y2 = np.array(insertion_sort_runtime)
y = []
for k in range(1, 100):
    y.append(np.array(tim_sort_runtime[k]))

plt.plot(x, y1, label="Merge Sort Runtime")
plt.plot(x, y2, label="Insertion Sort Runtime")
for k in range(1, 100):
    plt.plot(x, y[k - 1], label=f"Tim Sort Runtime with k={k}")

plt.legend(bbox_to_anchor=(1.55, 1), loc='upper right')
plt.show()