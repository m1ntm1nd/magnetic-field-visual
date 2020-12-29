import numpy as np
import matplotlib.pyplot as plt

def calc_x():
    return np.cos(np.linspace(0, 2*np.pi, 100))

def calc_y():
     return np.sin(np.linspace(0, 2*np.pi, 100))
    
def set_size(size):
    plt.figure(dpi=150)
    plt.xlim(-(size), (size))
    plt.ylim(-(size), (size))
    
def main():
    set_size(500)
    x = calc_x()
    y = calc_y()
    k = 1
    while k < 100:
        plt.plot(k*x-200,k*y,linewidth=0.5)
        plt.plot(k*x+200,k*y,linewidth=0.5)
        k+=2
    plt.show()
    print("blya")



if __name__ == "__main__":
    main()