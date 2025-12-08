# NS 1st Final Project code 
import random
locations = ["dawn winery", "starsnatch cliff", "nameless island", "ameno archon statue", 
             "stormbearer mountains", "springvale", "mondstadt city", "stormterror's lair", "starfell lake"]

print(locations)

location = input("what location do you want to explore?: ").lower()
if location == locations[0:9]:
    print(f"Time to explore {location} ")
else:
    print("Invalid location try again")

def Mondstadtcity():
    if location == locations[6]:
        print("welcome to Mondstadt city")

def statue():
    if location == statue:
        print("welcome to the Ameno Archon Statue")

def winery():
    if location == locations[0]:
        print(f"welcome to {locations[0]}")

def starsnatch():
    if location == starsnatch:
        print("welcome to Starsnatch Cliff")

def island():
     if location == island:
        print("welcome to the Nameless Island")

def stormbearers():
     if location == locations:
        print("Welcome to Stormbearer Mountains")

def springvale():
    if location == locations:
         print("Welcome to Springvale")

def stormterrors():
    if location == locations:
        print("Welcome to Stormterror Lair")

def starfell():
    if location == locations:
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
    combat_options = ["sword", "punch", "potion", "run away"]
    options = input("")
def HP():
    while player_HP <= 100:
        print("Your HP is low")
    if player_HP == 0:
        print("You died!")

inventory = {}

def player_inventory():