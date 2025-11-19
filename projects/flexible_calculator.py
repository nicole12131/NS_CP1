# NS, 1st period, Flexible Calculator

import statistics

# Calculator function using *args
def calculator(*args, operation="sum"):
    if operation == "sum":
        return sum(args)

    elif operation == "average":
        return statistics.mean(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

    elif operation == "product":
        product = 1
        for num in args:
            product *= num
        return product

    else:
        return "Invalid operation."


# Main Program (User Interface) 
print("Welcome to the Flexible Calculator!\n")
print("Available operations: sum, average, max, min, product\n")

keep_going = "yes"

while keep_going.lower() == "yes":
    # Ask user for operation
    operation = input("Which operation would you like to perform? ").lower()

    print("\nEnter numbers (type 'done' when finished):")
    numbers = []

    # Collect numbers until the user types 'done'
    while True:
        value = input("Number: ")

        if value.lower() == "done":
            break
        else:
            try:
                numbers.append(float(value))
            except ValueError:
                print("Please enter a valid number.")

    # Show what we're calculating
    numbers_text = ", ".join(str(n) for n in numbers)
    print(f"\nCalculating {operation} of: {numbers_text}")

    # Call the calculator function
    result = calculator(*numbers, operation=operation)

    print(f"Result: {result}\n")

    # Ask if user wants another calculation
    keep_going = input("Would you like to perform another calculation? (yes/no) ")

print("\nThank you for using the Flexible Calculator!")
