import matplotlib.pyplot as plt 
import numpy as np
def order(sentence):
    words = list(sentence.split(' '))
    ans = words.copy()
    for word in words:
        for symbol in word:
            if symbol.isdigit():
                ans[int(symbol)-1] = word
    return ans

class Provod(object):
  def __init__(self, pos = [0,0], power=[100,100]):
    self.pos = pos

    self.power = power

def find_angle(dot_x, dot_y, current_x, current_y):
  y = abs(dot_y - current_y)
  x = abs(dot_x - current_x)
  sin_a = y/(np.sqrt(x**2+y**2))
  return np.arcsin(sin_a)  #/np.pi*180


def find_c(_):
  pass

def calc_power(power,distance):
  


def main():
    size = 1000
    plt.figure(dpi=150)
    plt.xlim(-(size), (size))
    plt.ylim(-(size), (size))
    plt.grid()


   
    #plt.plot([0,0], [10,10], marker = 'o')
    # x_coord_1 = int(input("Enter x coord "))
    # y_coord_1 = int(input("Enter y coord "))
    # provod1 = Provod([x_coord_1,y_coord_1])
    # plt.scatter(provod1.pos[0],provod1.pos[1], s=5)
    # x_coord_2 = int(input("Enter x coord "))
    # y_coord_2 = int(input("Enter y coord "))
    # provod2 = Provod([x_coord_2,y_coord_2])
    # plt.scatter(provod2.pos[0],provod2.pos[1], s=5)
    #start_point_1 = [provod1.pos[0]+10,provod1.pos[1]]
    # x1, y1 = [-1, 12], [1, 4]
    # x2, y2 = [1, 10], [3, 2]
    # plt.plot(x1, y1, marker = 'o')
    # #plt.scatter(0,0,)
    # #случай с сонаправленными токами
    # theta = np.linspace(0, 2*np.pi, 100)
    # start_len = 10
    # size2 = size //10
    # alpha = 50
    # while size*10 > start_len:
    #   for i in theta:
    #     plt.plot(start_len*np.cos(theta),(start_len-alpha)*np.sin(theta),'--',linewidth=0.6)
    #   start_len *= 1.5
    # start_len = 10
    
    # # while size*10 > start_len:
    # #   for i in theta:
    # #     plt.plot((start_len*np.cos(theta)+alpha),start_len*np.sin(theta),'r',linewidth=0.6)
    # #   start_len *= 1.5
    #print(x_coord_1,y_coord_1)
    plt.show()



if __name__ == "__main__":
    main()



