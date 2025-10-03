# NS 1st ☑️While Loops Notes
import random
#for num(iterator) in range(1,21):break/end condition 
    #print(num) what loop does

#infinite loop
num = 1 

while num <=20:
    print(num)
    num += 1 #Prevents an infinite loop

goose = random.randint(1,20)
count = 0

while True:
    if count == goose:
        break
    else:
        print("duck")
else:
    print("GOOSE!")


i = 0 

while i < 20:
    if i == 10:
        print("i is 10 ")
        continue 
    else:
        print(f"{i} iteration of the loop")
    i+= 1

print("The loop ended! ")


""" ________
    |      O
     |    /|\\
     |    /\\
"""