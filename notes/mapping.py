# NS, 1st, Mapping Notes

numbers = [651,684,561,65,46,1,654,651,4]
'''new_nums = []

for num in numbers:
    new_nums.append(num/3)

print(new_nums)'''
def multiply(num):
    return num*num

new_nums = map(lambda num: num*3, numbers)
print(new_nums)
for num in new_nums:
    print(num)