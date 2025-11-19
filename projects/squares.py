# NS, 1st, Squared Numbers

# make the list of number that you want to squared
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]


def multiply(num):
    return num*num

new_nums = map(lambda num: num*num, numbers)
print(new_nums)
for number in numbers:
    squared = number*number
    print(f"Original: {number}, Squared: {squared}")