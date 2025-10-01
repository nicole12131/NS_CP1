# NS 1st 🔨 Shopping List Manager

shopping_list = []

while True:
    action = input("\nWhat do you want to do? (add / remove / print / exit): ").lower()

    if action == "add":
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(item + " has been added to your list.")

    elif action == "remove":
        item = input("Enter the item you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item + " has been removed from your list.")
        else:
            print("That item is not in your list.")

    elif action == "print":
        print("\nYour Shopping List:")
        if len(shopping_list) == 0:
            print("Your list is empty.")
        else:
            for i in range(len(shopping_list)):
                print(str(i + 1) + ". " + shopping_list[i])

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
