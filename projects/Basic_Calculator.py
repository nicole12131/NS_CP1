# NS 1st 🔨 Basic Calculator 

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str)
num2 = float(num2_str)

addition_result = num1 + num2
print(f"{num1} + {num2} = {addition_result:.2f}")
subtraction_result = num1 - num2
print(f"{num1} - {num2} = {subtraction_result:.2f}")
multiplication_result = num1 * num2
print(f"{num1} * {num2} = {multiplication_result:.2f}")
division_result = num1 / num2
print(f"{num1} / {num2} = {division_result:.2f}")
integer_division_result = num1 // num2
print(f"{num1} // {num2} = {integer_division_result:.2f}")
modulo_result = num1 % num2
print(f"{num1} % {num2} = {modulo_result:.2f}")
exponent_result = num1 ** num2
print(f"{num1} ** {num2} = {exponent_result:.2f}")