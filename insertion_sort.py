import matplotlib.pyplot as plt
import numpy as np

def insertion_sort_visualize(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        colors = ['green' if k < i else 'blue' for k in range(len(arr))]
        colors[i] = 'red'
        plt.bar(range(len(arr)), arr, color=colors)
        plt.pause(0.5)
        plt.clf()
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            temp = arr.copy()
            temp[j + 1] = key 
            colors = ['green' if k <= i else 'blue' for k in range(len(arr))]
            colors[j + 1] = 'red'
            plt.bar(range(len(arr)), temp, color=colors)
            plt.pause(0.5)
            plt.clf()
        arr[j + 1] = key
        colors = ['green' if k <= i else 'blue' for k in range(len(arr))]
        plt.bar(range(len(arr)), arr, color=colors)
        plt.pause(0.5)
        plt.clf()

siz = 15
arr = np.random.randint(0, 100, siz)
x = np.arange(0,siz,1)
plt.bar(x, arr, color='blue')
plt.pause(1)

insertion_sort_visualize(arr)

plt.bar(x, arr, color='purple')
plt.show()
