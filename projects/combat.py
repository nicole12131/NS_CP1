# NS 1st Combate Program 
import random

print("Welcome to training! First I need to know some things about you!\n")

name = input("What is your name?: ")

print("\nWhat class of fighter are you?")
print("1 - Fighter")
print("2 - Mage")
print("3 - Rogue")

choice = int(input("\nEnter your choice (1, 2, or 3): "))

health = 30
defense = 10
attack_bonus = 2
damage_bonus = 2
damage_die = 6
char_class = "Fighter"

if choice == 1:
    char_class = "Fighter"
    defense = 14
    attack_bonus = 3
    damage_bonus = 4
    damage_die = 8
elif choice == 2:
    char_class = "Mage"
    defense = 10
    attack_bonus = 4
    damage_bonus = 6
    damage_die = 10
elif choice == 3:
    char_class = "Rogue"
    defense = 12
    attack_bonus = 5
    damage_bonus = 3
    damage_die = 6
else:
    print("Invalid choice! You will be a Fighter by default.")

print("\nGreat, here are your stats:")
print("Class:", char_class)
print("Health:", health)
print("Defense:", defense)
print(f"Attack: D20 + {attack_bonus}")
print(f"Damage: D{damage_die} + {damage_bonus}")

# --- monster info ---
monster_name = "Dire Wolf"
monster_health = 35
monster_defense = 12
monster_attack_bonus = 3
monster_damage_die = 8
monster_damage_bonus = 2

print(f"\nYou are being attacked by a {monster_name}!")

player_turn_flag = random.choice([True, False])

if player_turn_flag:
    print("\nYou move first!\n")
else:
    print(f"\nThe {monster_name} moves first!\n")


def player_turn():
    global health, monster_health

    print("What would you like to do?")
    print("1 - Normal Attack")
    print("2 - Wild Attack (double damage but you hurt yourself a little)")
    print("3 - Drink a healing potion (regain 9 health)")
    print("4 - Flee (might escape!)")

    move = input("Choose (1-4): ")

    if move == "1":
        roll = random.randint(1, 20) + attack_bonus
        if roll >= monster_defense:
            dmg = random.randint(1, damage_die) + damage_bonus
            monster_health -= dmg
            print(f"\nYou hit the {monster_name} for {dmg} damage!")
        else:
            print("\nYou missed!")
    elif move == "2":
        roll = random.randint(1, 20) + attack_bonus
        if roll >= monster_defense:
            dmg = (random.randint(1, damage_die) + damage_bonus) * 2
            monster_health -= dmg
            recoil = random.randint(1, 4)
            health -= recoil
            print(f"\nYou go wild and deal {dmg} damage!")
            print(f"But you take {recoil} recoil damage!")
        else:
            print("\nYou swung wildly and missed!")
    elif move == "3":
        heal = 9
        health += heal
        print(f"\nYou drink a potion and regain {heal} health!")
    elif move == "4":
        escape = random.randint(1, 2)
        if escape == 1:
            print("\nYou got away safely!")
            return "fled"
        else:
            print(f"\nYou tried to flee but the {monster_name} blocked you!")
    else:
        print("\nYou hesitated and lost your turn!")

    if monster_health < 0:
        monster_health = 0

    print(f"\n{monster_name} now has {monster_health} health left.\n")


def monster_turn():
    global health
    roll = random.randint(1, 20) + monster_attack_bonus
    if roll >= defense:
        dmg = random.randint(1, monster_damage_die) + monster_damage_bonus
        health -= dmg
        print(f"The {monster_name} hits you for {dmg} damage!")
    else:
        print(f"The {monster_name} tries to bite you but misses!")

    if health < 0:
        health = 0

    print(f"You now have {health} health.\n")


while health > 0 and monster_health > 0:
    if player_turn_flag:
        result = player_turn()
        if result == "fled":
            break
        player_turn_flag = False
    else:
        monster_turn()
        player_turn_flag = True

if health <= 0:
    print("\nYou have been defeated... Game Over.")
elif monster_health <= 0:
    print(f"\nYou defeated the {monster_name}! Victory is yours!")
else:
    print("\nYou escaped successfully!")