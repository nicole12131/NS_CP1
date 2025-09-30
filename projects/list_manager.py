# NS 1st 🔨 Shopping List Manager

groceries = []

while True: 
    action = input("\n What do you want to do? (add, remove, view, exit): ").lower()
if action == "add":
    Item_add = input("What Item you want to add?: ")
    add_item(Item_add)
 