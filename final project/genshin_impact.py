# NS 1st Final Project code 
import random
locations = ["dawn winery", "starsnatch cliff", "nameless island", "ameno archon statue", 
             "stormbearer mountains", "springvale", "mondstadt city", "stormterror's lair", "starfell lake"]

print(locations)

location = input("what location do you want to explore?: ").lower()
if location in locations:
    print(f"Time to explore {location} ")
else:
    print("Invalid location try again")

def Mondstadtcity():
    if location == locations[6]:
        print("welcome to Mondstadt city")
        m = input("do you want to stay or go to another location?:  ")
        if m == "stay":
            print("Do you want to buy things or explore")
        else:
            print(")
        

def statue():
    if location == locations[3]:
        print("welcome to the Ameno Archon Statue")

def winery():
    if location == locations[0]:
        print(f"welcome to {locations[0]}")

def starsnatch():
    if location == locations[1]:
        print("welcome to Starsnatch Cliff")

def island():
     if location ==  locations[2]:
        print("welcome to the Nameless Island")

def stormbearers():
     if location ==  locations[4]:
        print("Welcome to Stormbearer Mountains")

def springvale():
    if location ==  locations[5]:
         print("Welcome to Springvale")

def stormterrors():
    if location ==  locations[7]:
        print("Welcome to Stormterror Lair")

def starfell():
    if location ==  locations[8]:
        print("Welcome to the Starfell Lake")

player_magic = 50
player_defense = 50
player_HP = 100
player_attack = 30
Player_inventory = {}


sword = random.randint(3,6)
punch = random.randint(1,3)
sword_potion = random.randint(6,12)
punch_potion = random.randint(2,6)

def combat():
    combat_options = ["sword", "punch", "potion", "run"]
    choice = input("Choose your action (sword/punch/potion/run): ").lower()

    if choice == "sword":
        print(f"You dealt {sword} damage!")
    elif choice == "punch":
        print(f"You punch for {punch} damage!")
    elif choice == "potion":
        print(f"You used a potion and restored {sword_potion} HP!")
    elif choice == "run":
        print("You ran away!")
    else:
        print("Invalid choice!")

def HP():
    while player_HP <= 100:
        print("Your HP is low")
    if player_HP == 0:
        print("You died!")

inventory = {}

