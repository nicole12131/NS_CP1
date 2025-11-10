# NS 1st Dictionaries Notes

#Key: Value pairs 

person = {
    #Key:value, 
    "name": "Xavier",
    "age": 22,
    "job": "Mavrick",
    "sibling": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"]
}

person_two = {
    "name": "Jake",
    "age": 21,
    "job": "NEET",
    "sibling": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier"]
}

print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in person[key]:
            print(f"{person['name']} has a sibling named {name}")
    else:
        print(f"{key} is {person[key]}")
# update values
print(person_two.values())
person_two["age"] -= 1 
print(person_two.items())
person_two["age"] -= 1 
person_two["SO"] = "Carry"
print(person_two.items())

