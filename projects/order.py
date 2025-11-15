# NS 1st Order Up!

#Create a dictionary called menu that stores drinks, mains, and sides with their prices

#SHOW the user the drink options
#ASK the user to choose a drink
#WHILE the drink is not in the menu
    #tell the user it's not valid
    #ask again

#SHOW the user the main course optionsH
#AHSK the user to choose a main course
#WHILE the main is not in the menu
    #tell the user it's not valid
    #ask again

#SHOW the user the side dish options
#ASK the user to choose the first side
#WHILE the side is not in the menu
    #tell the user it's not valid
    #ask again

#ASK the user to choose the second side
#WHILE the side is not in the menu
    #tell the user it's not valid
    #ask again

#CALCULATE the total cost by adding the prices of all four items

#PRINT the full order
#PRINT the total cost

menu = {
    "drinks": {
        "coke": 1.99,
        "sprite": 1.99,
        "water": 0.99,
        "tea": 1.49
    },
    "mains": {
        "burger": 7.49,
        "chicken": 6.99,
        "pizza": 5.49,
        "wrap": 6.49
    },
    "sides": {
        "fries": 2.49,
        "salad": 2.99,
        "rings": 2.79,
        "fruit": 2.59
    }
}

print("Drinks: coke, sprite, water, tea")
drink = input("Choose a drink: ").lower()
while drink not in menu["drinks"]:
    print("Not on the menu. Try again.")
    drink = input("Choose a drink: ").lower()

print("\nMain Courses: burger, chicken, pizza, wrap")
main = input("Choose a main course: ").lower()
while main not in menu["mains"]:
    print("Not on the menu. Try again.")
    main = input("Choose a main course: ").lower()

print("\nSide Dishes: fries, salad, rings, fruit")
side1 = input("Choose your first side: ").lower()
while side1 not in menu["sides"]:
    print("Not on the menu. Try again.")
    side1 = input("Choose your first side: ").lower()

side2 = input("Choose your second side: ").lower()
while side2 not in menu["sides"]:
    print("Not on the menu. Try again.")
    side2 = input("Choose your second side: ").lower()

total = (
    menu["drinks"][drink] +
    menu["mains"][main] +
    menu["sides"][side1] +
    menu["sides"][side2]
)

print("\nYour Order:")
print("Drink:", drink.title())
print("Main Course:", main.title())
print("Side Dishes:")
print(side1.title())
print(side2.title())
print("Total Cost: $", round(total, 2))
