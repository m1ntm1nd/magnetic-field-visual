import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm

def set_size(size):
    plt.figure(dpi=150)
    plt.xlim(-(size), (size))
    plt.ylim(-(size), (size))
    plt.grid()


def calculate_b(power, amperage = 1, length = 1):
    return power / amperage / length


def calc_len(x,y,x1,y1):
    return np.sqrt((x-x1)**2+(y-y1)**2)

x_axes = np.linspace(-10,10,10000)
y_axes = np.linspace(-10,10,10000)
cnt = 0
list3 = [] 
for i in x_axes:
    list3.append([x_axes[cnt],y_axes[cnt],calc_len(x_axes[cnt],y_axes[cnt],0,0)])
    cnt+=1
arr = np.array(list3)
print(arr)

set_size(10)
for i in arr:
    if round(i[2],1) == 14.1:
        plt.plot(i[0],i[1])
plt.show()

