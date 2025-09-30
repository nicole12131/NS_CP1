# NS 1st 🔨 Shopping List Manager

# The main shopping list variable
shopping_list = []

# --- Function Definitions ---

def add_item(item):
    """Adds a new item to the shopping list."""
    shopping_list.append(item.strip().capitalize())
    print(f"\n✅ '{item.capitalize()}' added to the list.")

def remove_item(item):
    """Removes an item from the shopping list if it exists."""
    item_to_remove = item.strip().capitalize()
    try:
        shopping_list.remove(item_to_remove)
        print(f"\n🗑️ '{item_to_remove}' removed from the list.")
    except ValueError:
        print(f"\n❌ Error: '{item_to_remove}' is not in the list.")

def view_list():
    """Prints the current shopping list."""
    if not shopping_list:
        print("\n🛒 Your shopping list is currently empty!")
        return

    print("\n--- Your Shopping List ---")
    # Use enumerate to display items with a numbered index starting from 1
    for index, item in enumerate(shopping_list, 1):
        print(f"{index}. {item}")
    print("--------------------------")

# --- Main Program Loop ---
while True:
    # User input with instructions
    action = input("\nWhat would you like to do? (add, remove, view, exit): ").strip().lower()

    # --- Write your code here ---
    if action == "add":
        new_item = input("Enter the item to add: ")
        if new_item:
            add_item(new_item)
        view_list() # Print the list after the change

    elif action == "remove":
        item_to_remove = input("Enter the item to remove: ")
        if item_to_remove:
            remove_item(item_to_remove)
        view_list() # Print the list after the change

    elif action == "view":
        view_list()

    elif action == "exit":
        break

    else:
        print("\n⚠️ Invalid action. Please enter 'add', 'remove', 'view', or 'exit'.")

print("\n👋 Thanks for using the Shopping List Manager! Goodbye.")