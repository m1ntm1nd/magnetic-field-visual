import matplotlib.pyplot as plt 

def order(sentence):
    words = list(sentence.split(' '))
    ans = words.copy()
    for word in words:
        for symbol in word:
            if symbol.isdigit():
                ans[int(symbol)-1] = word
    return ans

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
    print(start_guide())
    # dev_x = [1 , 10, 100, 1000]
    # dev_y = [10 , 25, 50, 125]
    # dev_y_2 = [100 , 250, 500, 1250]
    # plt.plot(dev_x, dev_y,label="eblo")
    # plt.plot(dev_x, dev_y_2,label="tablo")
    # # plt.legend(['Ebloids', 'Tabloids'])
    # plt.xlabel("lol")
    # plt.ylabel("kek")
    # plt.title("idi nahyi")  
    # plt.show()
    # pass


if __name__ == "__main__":
    main()



