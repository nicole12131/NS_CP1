# NS 1st Formatting outputs notes

# How do I write the format method?
name = "Jake"
age = 1200
money = 25.1
percent = .74

print("Hello {}, you are {}. That is so old! You have ${: .2f} you most be rich! Random percent is {:%}. ".format(name, age, money, percent))


print(f"Hello {name}, you are {age:,}. That is so old! You have ${money:.2f} you must be rich! Random percent is {88/100:.1f}%.")