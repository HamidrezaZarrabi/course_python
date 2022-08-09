import numpy as np
import sys

a = int(input("Please enter your number: "))
operation = input("Please choose your desired operator from (+, -, *, /, radical, sin, cos, tan, cot, factorial): ")
if operation in ["+", "-", "*", "/"]:
    b = int(input("Please enter your second number: "))
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
elif operation == "radical":
    result = np.sqrt(a)
elif operation == "sin":
    a_radian = (a / 180 * np.pi)
    result = np.sin(a_radian)
elif operation == "cos":
    a_radian = (a / 180 * np.pi)
    result = np.cos(a_radian)
elif operation == "tan":
    a_radian = (a / 180 * np.pi)
    result = np.tan(a_radian)
elif operation == "cot":
    a_radian = (a / 180 * np.pi)
    result = 1/ np.tan(a_radian)
elif operation == "factorial":
    result = np.math.factorial(a)
else:
    print('You have chosen a wrong operator')
    sys.exit()
print("Result: ", result)