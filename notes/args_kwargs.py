# NS 1st *args and **kwatgs Notes


'''def hello(name = "Tia", age=29):
    return f"Hello {name}! You are {age}"


print(hello())
print(hello("Treyson", 19))
print(hello("Vienna"))'''


def hello(*names, **kwargs):
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"Hello {n} {kwargs['Last_name']}")

hello("Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake", last_name="LaRose", dad = "Eric", num_cats=5)


def full_name(age, **names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']} is {age}"
    else:
        return f"{names['first']} {names['last']} is {age}"
    
print(full_name(age = "???", first="Koro", last="Sensei"))
print(full_name(age = "So old", first="Albus", middle="Brian", last="Dumbuldore"))

def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum+= f"{story["name"]} is the main character of this story."
    if "place" in story.keys():
        sum+= f"The story takes place in {story['place']}."
    if "conflict" in story.keys():
        sum+= f"The problem ins {story['conflict']}."

    return sum

print(summary(name ="Luke Skywalker", place="a galaxy far far away"))
print(summary(name ="Harry Potter", conflict="Evil wizard wants to kill him"))