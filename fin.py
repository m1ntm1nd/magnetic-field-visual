import numpy as np
import matplotlib.pyplot as plt



def console_interface():
    mas = []
    i = int(input('amount of wires = '))
    for j in range(i):
        x = int(input('x = '))
        y = int(input('x = '))
        mas.append((x, y))



def main():
    x, y = np.mgrid[0:10:1000j, 0:10:1000j]

    #Формулы

    x_1, x_2, y_0 = 4, 6, 5
    y_2 = 6
    d = x_2 - x_1
    r_1 = np.sqrt((x - x_1)**2 + (y - y_0)**2)
    r_2 = np.sqrt((x - x_2)**2 + (y - y_2)**2)
    a = (d**2 - r_1**2 - r_2**2)/(2*r_1*r_2)
    B_1 = 1/(2*np.pi*(r_1))
    B_2 = (5/(2*np.pi*(r_2)))
    B = 10*np.sqrt(B_1**2 + B_2**2 + 2*B_1*B_2*np.cos(a))


    fig, axes = plt.subplots()
    lev = [1, 2, 3, 4, 6, 10, 20, 40, 100, 900]

    #  Контуры разного цвета:
    color_line = np.zeros((10, 3))
    color_line[:, 1:] = 0.1
    color_line[:, 0] = np.linspace(0, 1, 10)


    axes.contour(x, y, B, levels = lev,
            colors = color_line)
    axes.set_title('Линии магнитного поля параллельных проводников в плоскости:')

    fig.set_figwidth(12)    
    fig.set_figheight(6)  
    plt.show()


if __name__ == "__main__":
    main()
