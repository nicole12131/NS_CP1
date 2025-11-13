# NS 1st Order Up!
#make the menu 
menu = {
    "Drinks": ["Coca cola"],
    "Main Courses": [],
    "Side Dishes": [],
}
# User order 
Your_order = {
    "Drink": "",
    "Main Course": "",
    "Side dishes": "",
    "Total cost": "",
}

# 
drink = input("What ")
main_course = input()
side_dishes = input()

if drink == menu:
    Your_order["Drink"] = drink
else: 
    print()

print(Your_order.items())