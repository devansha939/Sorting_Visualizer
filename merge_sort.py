import matplotlib.pyplot as plt
import numpy as np

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1].copy() 
    R = arr[m + 1:r + 1].copy()
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_visualize(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_visualize(arr, l, m)
        merge_sort_visualize(arr, m + 1, r)
        merge(arr, l, m, r)
        plt.bar(range(len(arr)), arr, color='blue')
        plt.bar(range(l, r + 1), arr[l:r + 1], color='green')
        plt.pause(0.5)
        plt.clf()

siz = 15
arr = np.random.randint(0, 100, siz)
x = np.arange(0, siz, 1)

plt.bar(x, arr, color='blue')
plt.pause(1)
plt.clf()
merge_sort_visualize(arr, 0, siz - 1)

plt.bar(x, arr, color='purple')
plt.show()
