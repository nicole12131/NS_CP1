# NS 1st For loops Notes

import time

nums = [4,654,136,84,651,86,42,1,564,3,4894]

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number")
    else:
        print(num)

print("The loop is over")   

health = 15

for num in range(1,health,2):
    print(num)
    time.sleep(200)

for num in range(20,0,-2):
    print(num)