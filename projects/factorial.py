# NS 1st Factorial Calculator

# define function multiply(*args)
    # set product
    #loop through args:
        # multiply prduct by currentary
        # return product
# Define function factorial(original_num):
    # set num to original num 
    # set nums to an empty list
    # loop while num > 1:
        # subtract 1 from num
        # add num to num list
    #return multiply(*nums)
#Display "welcome to the factorial calculator"
#Display "Please neter a whole number that is great than 0"
# Loop forever
    #user_num = take user input
    # if user_num is an integer:
        # if user_num is greater than 0:
            # Exit loop 
        # otherwise
            #Display "Number must be greater than 0 "
        # otherwise
            #Display "must be a whole number"
# factorial(user_num)


    
def multiply(*args):
    product = 1
    for value in args:
        product *= value
    return product


def factorial(original_num):
    num = original_num
    nums = []
    
    # Build a list of numbers from n down to 1
    while num > 1:
        nums.append(num)
        num -= 1

    return multiply(*nums)


print("Welcome to the factorial calculator!")
print("Please enter a whole number that is greater than 0")

# Get a valid input
while True:
    user_input = input("Enter a number: ")

    if user_input.isdigit():             # check if whole number
        user_num = int(user_input)
        if user_num > 0:                 # check if > 0
            break
        else:
            print("Number must be greater than 0.")
    else:
        print("Must be a whole number.")

result = factorial(user_num)
print(f"The factorial of {user_num} is {result}.")
