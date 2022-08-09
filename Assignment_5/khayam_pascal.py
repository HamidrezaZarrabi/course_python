import numpy as np

a = int(input('Please enter your number: '))
triangle = np.zeros((a, a))
for m in range(a):
    triangle[m, 0] = 1
    for n in range(1, m):
        triangle[m, n] = triangle[m-1, n] + triangle[m-1, n-1]
    triangle[m, m] = 1
print(triangle)

for m in range(a):
    for n in range(m+1):
        print(triangle[m, n], end='\t')
    print()
