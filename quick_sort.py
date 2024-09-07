import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high):
    pivot = arr[high]  
    i = low 
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i ], arr[high] = arr[high], arr[i ]
    return i 

def quick_sort_visualize(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        plt.bar(x, arr, color=['green' if i < low else 'red' if i == pi else 'blue' for i in range(len(arr))])
        plt.pause(0.5)
        plt.clf()
        quick_sort_visualize(arr, low, pi - 1)
        quick_sort_visualize(arr, pi + 1, high)

siz = 15
arr = np.random.randint(0, 100, siz)
x = np.arange(0, siz, 1)

plt.bar(x, arr, color='blue')
plt.pause(1)
plt.clf()

quick_sort_visualize(arr, 0, siz - 1)

plt.bar(x, arr, color='purple')
plt.show()
