a = int(input('Please enter first number: '))
b = int(input('Please enter second number: '))

if a < b: a, b = b, a

for gcd in range(b, 0, -1):
    if b % gcd == 0 and a % gcd == 0:
        print('Greatese common divisor is: ', gcd)
        break
