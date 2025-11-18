# NS, 1st period, Flexible Calculator
import time as t
import random as r

print("welcome to the Flexible Calculator!")
print("Available operations: sum, average, max, min, product")

available_operations = ["sum", "average", "max", "min", "product"]
operation = input("which operation would you like to perfrom?: ")

while True:
    if operation == available_operations:
        numbers = input("Enter numbers (type 'done' when finished): ")
    else:
        print(" That’s not a valid option, try again") 

