import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation
import numpy as np
from math import sin , cos, pi
from tqdm import tqdm
import numba as nb
from numba import jit


def E1(q_prop, xs, ys):# для n-ого числа зарядов
    l=1
    k=9*10**9
    dx=0
    dy=0
    c=0

    for c in range(len(q_prop)):
      q=q_prop[c]
      r=((xs-q[0])**2+(ys-q[1])**2)**0.5
      v=(k*q[2])/r**2
      x=(xs-q[0])*(v/r)
      y=(ys-q[1])*(v/r)
      dx+=x
      dy+=y

    return np.array([dx, dy])

def start_guide():
  print("Enter how many electric charges to emplace: (to see example type 0)")
  n = int(input())
  if n == 0:
    return [[-60, 0, 10**(-9),1],[60, 0, -10**(-9),1]]
  ans = []
  for i in range(n):
    print("Type x_coord, y_coord, (in range |150|) and sign of charge (+ or - ) in format (x y +)")
    data = list(input().split(' '))
    if data[2] == '+':
      data[2] = 10**(-9)
    else:
      data[2] = -10**(-9)
    data.append(1)
    ans.append(data)
  return ans

def main():
  size = 150 #size of plot
  plt.figure(dpi=150)
  plt.xlim(-(size+1), (size+1))
  plt.ylim(-(size+1), (size+1))
  kof=0.001

  q_prop=np.array(start_guide())
  wind=np.zeros(int(2*np.pi*10))

  #q_prop=np.array([[-150000000*kof, 700000*kof, 50*10**(-9),0], [-150000000*kof, -700000*kof, -50*10**(-9),0], [0*kof, 6400*kof, 2*10**(-9),1],[0*kof, -6400*kof, -2*10**(-9),1]])

  n=20  #lines num

  r_q = np.sqrt(15)
  plt.gca().set_aspect('equal', adjustable='box')
  theta = np.linspace(0, 2*np.pi, n)
  mask=q_prop[ q_prop[:,2]>0 ][ q_prop[q_prop[:,2]>0][:,3]==1 ]


  for cq, q in enumerate(mask):
    x11 = r_q*np.cos(theta)+q[0]
    x22 = r_q*np.sin(theta)+q[1]
    for xs, ys in tqdm(zip(x11, x22)):
      lines=[[],[]]
      
      stop=0
      
      lines[0].append(xs)
      lines[1].append(ys)      
      while  abs(xs)<size+2 and abs(ys)<size+2: 
        for cq1, q in enumerate(q_prop):
          if ((ys-q[1])**2+(xs-q[0])**2)**0.5<r_q/2 :#and cq1!=cq
            stop=1
            break
        if stop==1:
          break
        dx, dy = E1(q_prop,xs,ys)

        xs+=dx
        ys+=dy
        lines[0].append(xs)
        lines[1].append(ys)      
        
      plt.plot(lines[0],lines[1], c="r", linewidth=0.8)

  plt.scatter(q_prop[:,0],q_prop[:,1], s=r_q*30)
  for q in q_prop:
    if q[2]>0:
      plt.text(q[0], q[1], "+", fontsize=10)
    else:
      plt.text(q[0], q[1], "-", fontsize=20)


  plt.show()



if __name__ == "__main__":
    main()