import matplotlib.pyplot as plt
import numpy as np

def selection_sort_visualize(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        colors = ['blue'] * len(arr)
        colors[min_idx] = 'red' 
        plt.bar(range(len(arr)), arr, color=colors)
        plt.pause(0.5)
        plt.clf()
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        colors = ['blue'] * len(arr)
        plt.bar(range(len(arr)), arr, color=colors)
        plt.bar(range(i + 1), arr[:i + 1], color='green')
        plt.pause(0.5)
        plt.clf()

siz = 15
arr = list(np.random.randint(0, 100, siz))
x = np.arange(0, siz, 1)
plt.bar(x, arr, color='blue')
plt.pause(1)
plt.clf()
selection_sort_visualize(arr)
plt.bar(x, arr, color='purple')
plt.show()
