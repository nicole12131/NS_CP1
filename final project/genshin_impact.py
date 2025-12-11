# NS 1st Final Project code 
import random


locations = [
    "Dawn Winery",
    "Starsnatch Cliff",
    "Nameless Island",
    "Anemo Archon Statue",
    "Stormbearer Mountains",
    "Springvale",
    "Mondstadt City",
    "Stormterror's Lair",
    "Starfell Lake"
]


player_stats = {
    "HP": 30,
    "Attack": 5,
    "Defense": 3,
    "Magic": 2,
    "EXP": 0,
    "Level": 1
}

inventory = []
enemies_alive = {
    "Cryo Slime": True,
    "Hilichurl": True,
    "Ruin Guard": True,
    "Eye of the Storm": True,
    "Abyss Mage": True,
    "Stormterror": True,
}

items_on_ground = {
    "Sword": "Starsnatch Cliff",
    "Flower": "Starsnatch Cliff",
    "Dandelion Seed": "Stormbearer Mountains",
    "Valberry": "Stormbearer Mountains",
    "Fish": "Starfell Lake",
    "Potion": "Springvale"
}



def choose_location():
    print(locations)
while True:
        choice = input("\nWhere do you want to go? ").strip()
if choice in locations:
    return choice
else:
        print("Invalid location, try again.")


def stay_or_go():
    while True:
        choice = input("Stay or go to another location? (stay/go): ").lower()
    if choice in ["stay", "go"]:
        return choice
    else:
        print("Invalid choice, try again.")



def mondstadt_city():
    print("\nYou arrive at Mondstadt City.")
    choice = stay_or_go()
    if choice == "stay":
        print("You visit shops and explore the city.")
    else:
        return choose_location()


def anemo_archon_statue():
    print("\nYou arrive at the Anemo Archon Statue.")
    choice = stay_or_go()
    if choice == "stay":
        print("You explore the peaceful statue grounds.")
    else:
        return choose_location()


def dawn_winery():
    print("\nYou arrive at Dawn Winery.")
    choice = stay_or_go()

    if choice == "stay":
        print("You encounter local monsters nearby.")

        if enemies_alive["Cryo Slime"]:
            combat("Cryo Slime", 10)
            enemies_alive["Cryo Slime"] = False

        if enemies_alive["Hilichurl"]:
            combat("Hilichurl", 12)
            enemies_alive["Hilichurl"] = False

    else:
        return choose_location()


def starsnatch_cliff():
    print("\nYou climb to Starsnatch Cliff.")
    choice = stay_or_go()

    if choice == "stay":
        print("You explore for swords and flowers.")

        for item, loc in items_on_ground.items():
            if loc == "Starsnatch Cliff":
                print(f"You found a {item}!")
                inventory.append(item)
                items_on_ground[item] = None

        if enemies_alive["Ruin Guard"]:
            combat("Ruin Guard", 25)
            enemies_alive["Ruin Guard"] = False

        if enemies_alive["Eye of the Storm"]:
            combat("Eye of the Storm", 18)
            enemies_alive["Eye of the Storm"] = False

    else:
        return choose_location()


def nameless_island():
    print("\nYou arrive at Nameless Island.")
    choice = stay_or_go()

    if choice == "stay":
        print("You explore a mysterious empty island.")
    else:
        return choose_location()


def stormbearer_mountains():
    print("\nYou travel to Stormbearer Mountains.")
    choice = stay_or_go()

    if choice == "stay":

        for item, loc in list(items_on_ground.items()):
            if loc == "Stormbearer Mountains":
                print(f"You picked up {item}.")
                inventory.append(item)
                items_on_ground[item] = None

        print("You encounter multiple enemies!")

        if enemies_alive["Abyss Mage"]:
            combat("Abyss Mage", 15)
            enemies_alive["Abyss Mage"] = False

    else:
        return choose_location()


def springvale():
    print("\nYou enter Springvale.")
    choice = stay_or_go()

    if choice == "stay":
        print("You explore the friendly village.")

        if items_on_ground.get("Potion") == "Springvale":
            print("You found a Potion!")
            inventory.append("Potion")
            items_on_ground["Potion"] = None

    else:
        return choose_location()


def stormterror_lair():
    print("\nYou enter Stormterror’s Lair.")
    choice = stay_or_go()

    if choice == "stay":
        print("Dangerous enemies surround you!")

        if enemies_alive["Stormterror"]:
            print("⚠ The FINAL BOSS Stormterror appears!")
            combat("Stormterror", 35)
            enemies_alive["Stormterror"] = False
            print("Stormterror is now on your side!")
        else:
            print("Stormterror has already been defeated.")

    else:
        return choose_location()


def starfell_lake():
    print("\nYou arrive at Starfell Lake.")
    choice = stay_or_go()

    if choice == "stay":

        # pick fish
        if items_on_ground.get("Fish") == "Starfell Lake":
            print("You caught some fish!")
            inventory.append("Fish")
            items_on_ground["Fish"] = None

        if enemies_alive["Hilichurl"]:
            combat("Hilichurl", 10)
            enemies_alive["Hilichurl"] = False

    else:
        return choose_location()



def combat(enemy, enemy_hp):
    print(f"\n⚔ Combat started against {enemy}!")

    while enemy_hp > 0 and player_stats["HP"] > 0:
        print(f"\nYour HP: {player_stats['HP']}\n{enemy}'s HP: {enemy_hp}")
        action = input("Choose action (punch/sword/potion/run): ").lower()

        if action == "punch":
            dmg = random.randint(1, 3) + player_stats["Attack"]
            enemy_hp -= dmg
            print(f"You punch for {dmg} damage!")

        elif action == "sword":
            if "Sword" in inventory:
                dmg = random.randint(3, 6) + player_stats["Attack"]
                enemy_hp -= dmg
                print(f"You slash with your sword for {dmg} damage!")
            else:
                print("You don't have a sword!")

        elif action == "potion":
            show_inventory()
            continue

        elif action == "run":
            print("You ran away!")
            return

        else:
            print("Invalid action.")
            continue

        # Enemy attacks back
        if enemy_hp > 0:
            enemy_dmg = random.randint(1, 5) - player_stats["Defense"]
            enemy_dmg = max(0, enemy_dmg)
            player_stats["HP"] -= enemy_dmg
            print(f"{enemy} hits you for {enemy_dmg} damage!")

    # Combat results
    if player_stats["HP"] <= 0:
        death_screen()

    print(f"\nYou defeated {enemy}!")
    player_stats["EXP"] += 5
    check_level_up()


def show_inventory():
    print("\nInventory:", inventory)
    choice = input("Use or remove an item? (use/remove/back): ").lower()

    if choice == "use":
        item = input("Which item? ")

        if item not in inventory:
            print("Item not found.")
            return
        
        if item == "Potion":
            player_stats["HP"] += 10
            print("You used a Potion and recovered 10 HP!")
            inventory.remove(item)

        else:
            print("You can't use that item now.")

    elif choice == "remove":
        item = input("Which item? ")

        if item not in inventory:
            print("Item not found.")
            return

        inventory.remove(item)
        print(f"{item} removed from inventory.")

    elif choice == "back":
        return



def check_level_up():
    if player_stats["EXP"] >= 10:
        print("\n🎉 LEVEL UP! All stats increased!")
        player_stats["Level"] += 1
        player_stats["Attack"] += 2
        player_stats["Defense"] += 2
        player_stats["Magic"] += 2
        player_stats["HP"] += 10
        player_stats["EXP"] = 0



def death_screen():
    print("\n💀 You have died.")
    choice = input("Do you want to restart the game? (yes/no): ").lower()

    if choice == "yes":
        main_game_loop()
    else:
        print("Thanks for playing!")
        exit()



def main_game_loop():
    print("\nWelcome to your adventure!")
    current_location = choose_location()

    while True:

        if current_location == "Mondstadt City":
            current_location = mondstadt_city()
        elif current_location == "Anemo Archon Statue":
            current_location = anemo_archon_statue()
        elif current_location == "Dawn Winery":
            current_location = dawn_winery()
        elif current_location == "Starsnatch Cliff":
            current_location = starsnatch_cliff()
        elif current_location == "Nameless Island":
            current_location = nameless_island()
        elif current_location == "Stormbearer Mountains":
            current_location = stormbearer_mountains()
        elif current_location == "Springvale":
            current_location = springvale()
        elif current_location == "Stormterror's Lair":
            current_location = stormterror_lair()
        elif current_location == "Starfell Lake":
            current_location = starfell_lake()

        if current_location is None:
            current_location = choose_location()

