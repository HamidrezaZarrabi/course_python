a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))

if b > a: a, b = b, a
for lcm in range(a, a*b+1):
    if lcm % b == 0 and lcm % a == 0:
        print('Least common multiple is: ', lcm)
        break
