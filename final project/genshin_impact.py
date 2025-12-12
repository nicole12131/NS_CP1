# NS 1st Final Project code 
import random

locations = [
    "dawn winery",
    "starsnatch cliff",
    "nameless island",
    "anemo archon statue",
    "stormbearer mountains",
    "springvale",
    "mondstadt city",
    "stormterror's lair",
    "starfell lake"
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
    "cryo slime": True,
    "hilichurl": True,
    "ruin guard": True,
    "eye of the storm": True,
    "abyss mage": True,
    "stormterror": True
}

items_on_ground = {
    "sword": "starsnatch cliff",
    "flower": "starsnatch cliff",
    "dandelion seed": "stormbearer mountains",
    "valberry": "stormbearer mountains",
    "fish": "starfell lake",
    "potion": "springvale"
}

def choose_location():
    print("\nLocations you can go to:")
    print([loc.title() for loc in locations])

    while True:
        loc = input("Where do you want to go?: ").lower()
        if loc in locations:
            return loc
        else:
            print("Invalid location, try again.")


def stay_or_go():
    while True:
        choice = input("Stay here or go somewhere else? (stay/go): ").lower()
        if choice in ["stay", "go"]:
            return choice
        else:
            print("Invalid choice, try again.")

def mondstadt_city():
    print("You arrive at Mondstadt City.")
    if stay_or_go() == "stay":
        print("You look around, visit shops, and relax.")
    else:
        return choose_location()


def anemo_archon_statue():
    print("You arrive at the Anemo Archon Statue.")
    if stay_or_go() == "stay":
        print("You take in the peaceful view of the wind statue.")
    else:
        return choose_location()


def dawn_winery():
    print("You arrive at Dawn Winery.")
    if stay_or_go() == "stay":
        print("Some monsters appear nearby!")

        if enemies_alive["cryo slime"]:
            combat("cryo slime", 10)
            enemies_alive["cryo slime"] = False

        if enemies_alive["hilichurl"]:
            combat("hilichurl", 12)
            enemies_alive["hilichurl"] = False
    else:
        return choose_location()


def starsnatch_cliff():
    print("You climb Starsnatch Cliff.")
    if stay_or_go() == "stay":
        print("You search the cliff for items.")

        for item, loc in list(items_on_ground.items()):
            if loc == "starsnatch cliff":
                print(f"You found a {item}!")
                inventory.append(item)
                items_on_ground[item] = None

        if enemies_alive["ruin guard"]:
            combat("ruin guard", 25)
            enemies_alive["ruin guard"] = False

        if enemies_alive["eye of the storm"]:
            combat("eye of the storm", 18)
            enemies_alive["eye of the storm"] = False

    else:
        return choose_location()


def nameless_island():
    print("You arrive at a mysterious nameless island.")
    if stay_or_go() == "stay":
        print("It's quiet... maybe too quiet.")
    else:
        return choose_location()


def stormbearer_mountains():
    print("You head into Stormbearer Mountains.")
    if stay_or_go() == "stay":

        for item, loc in list(items_on_ground.items()):
            if loc == "stormbearer mountains":
                print(f"You picked up {item}.")
                inventory.append(item)
                items_on_ground[item] = None

        if enemies_alive["abyss mage"]:
            combat("abyss mage", 15)
            enemies_alive["abyss mage"] = False
    else:
        return choose_location()


def springvale():
    print("You walk into Springvale, a calm little village.")
    if stay_or_go() == "stay":

        if items_on_ground.get("potion") == "springvale":
            print("You found a Potion!")
            inventory.append("potion")
            items_on_ground["potion"] = None
    else:
        return choose_location()


def stormterror_lair():
    print("You step into Stormterror's Lair.")
    if stay_or_go() == "stay":
        print("The air is tense...")

        if enemies_alive["stormterror"]:
            print("STORMTERROR APPEARS! Final boss time!")
            combat("stormterror", 35)
            enemies_alive["stormterror"] = False
            print("Stormterror has been defeated!")
        else:
            print("Stormterror is already gone.")
    else:
        return choose_location()


def starfell_lake():
    print("You arrive at Starfell Lake.")
    if stay_or_go() == "stay":
        if items_on_ground.get("fish") == "starfell lake":
            print("You caught some fish!")
            inventory.append("fish")
            items_on_ground["fish"] = None

        if enemies_alive["hilichurl"]:
            combat("hilichurl", 10)
            enemies_alive["hilichurl"] = False

    else:
        return choose_location()

def combat(enemy, enemy_hp):
    print(f"A {enemy.title()} attacks you!")

    while enemy_hp > 0 and player_stats["HP"] > 0:
        print(f"\nYour HP: {player_stats['HP']}")
        print(f"{enemy.title()} HP: {enemy_hp}")

        move = input("Attack with punch/sword/potion or run: ").lower()

        if move == "punch":
            dmg = random.randint(1, 3) + player_stats["Attack"]
            enemy_hp -= dmg
            print(f"You punch for {dmg} damage!")

        elif move == "sword":
            if "sword" in inventory:
                dmg = random.randint(3, 6) + player_stats["Attack"]
                enemy_hp -= dmg
                print(f"You slash with your sword for {dmg} damage!")
            else:
                print("You don't have a sword!")

        elif move == "potion":
            show_inventory()
            continue

        elif move == "run":
            print("You escaped!")
            return
        else:
            print("Invalid move.")
            continue

        if enemy_hp > 0:
            hurt = random.randint(1, 5) - player_stats["Defense"]
            hurt = max(hurt, 0)
            player_stats["HP"] -= hurt
            print(f"The {enemy} hits you for {hurt} damage!")

    if player_stats["HP"] <= 0:
        death_screen()

    print(f"You defeated the {enemy}!")
    player_stats["EXP"] += 5
    check_level_up()

def show_inventory():
    print("Your Inventory:", inventory)
    choice = input("Use item, remove item, or go back? (use/remove/back): ").lower()

    if choice == "use":
        item = input("Which item do you want to use?: ").lower()

        if item not in inventory:
            print("You don't have that.")
            return

        if item == "potion":
            player_stats["HP"] += 10
            print("You used a potion and healed 10 HP!")
            inventory.remove(item)
        else:
            print("You can't use that here.")

    elif choice == "remove":
        item = input("Which item do you want to remove?: ").lower()

        if item in inventory:
            inventory.remove(item)
            print(f"{item} removed.")
        else:
            print("You don't have that.")

    else:
        return

def check_level_up():
    if player_stats["EXP"] >= 10:
        print("\nLEVEL UP! You feel stronger!")
        player_stats["Level"] += 1
        player_stats["Attack"] += 2
        player_stats["Defense"] += 2
        player_stats["Magic"] += 2
        player_stats["HP"] += 10
        player_stats["EXP"] = 0


def death_screen():
    print("\nYou have died.")
    again = input("Do you want to restart? (yes/no): ").lower()
    if again == "yes":
        main_game_loop()
    else:
        print("Game Over.")
        exit()


def main_game_loop():
    print("Welcome to your adventure!")

    current_location = choose_location()

    while True:
        if current_location == "mondstadt city":
            current_location = mondstadt_city()
        elif current_location == "anemo archon statue":
            current_location = anemo_archon_statue()
        elif current_location == "dawn winery":
            current_location = dawn_winery()
        elif current_location == "starsnatch cliff":
            current_location = starsnatch_cliff()
        elif current_location == "nameless island":
            current_location = nameless_island()
        elif current_location == "stormbearer mountains":
            current_location = stormbearer_mountains()
        elif current_location == "springvale":
            current_location = springvale()
        elif current_location == "stormterror's lair":
            current_location = stormterror_lair()
        elif current_location == "starfell lake":
            current_location = starfell_lake()

        # If a location function returns None, choose again
        if current_location is None:
            current_location = choose_location()

main_game_loop()
