import numpy as np

if __name__ == '__main__':
    length = int(input('Enter length of rhombus: '))
    rhombus = np.zeros((2*length-1, 2*length-1))
    x_center = length - 1
    for m in range(length):
        rhombus[m, x_center-m:x_center+m+1] = 1
        rhombus[2*length - 2 - m, x_center-m:x_center+m+1] = 1
    for m in range(rhombus.shape[0]):
        for n in range(rhombus.shape[1]):
            if rhombus[m][n] == 1:
                print("*", end='')
            else:
                print(' ', end='')
        print()