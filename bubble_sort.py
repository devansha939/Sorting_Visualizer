import matplotlib.pyplot as plt
import numpy as np

siz = 15
lst = np.random.randint(0, 100, siz)
x = np.arange(0, siz, 1)
sorted_colors = ['blue'] * siz

for i in range(siz):
    for j in range(0, siz-i-1):
        colors = sorted_colors.copy()
        colors[j] = 'red'
        colors[j+1] = 'red'
        plt.bar(x, lst, color=colors)
        plt.pause(0.1)
        plt.clf()
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
    sorted_colors[siz-i-1] = 'green'

sorted_colors = ['purple'] * siz
plt.bar(x, lst, color=sorted_colors)
plt.show()
