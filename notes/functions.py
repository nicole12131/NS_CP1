# NS 1st Functions Notes 
#Set variables

#define functions 
def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]

        return initials

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0 
while x < add(3,9):
    print("duck")
    x+=1

print("Goose!")

