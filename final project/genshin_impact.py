# NS 1st Final Project code 
import random
locations = ["dawn winery", "starsnatch cliff", "nameless island", "ameno archon statue", 
             "stormbearer mountains", "springvale", "mondstadt city", "stormterror's lair", "starfell lake"]

print(locations)

location = input("what location do you want to explore?: ").lower()
while True:
    if location in locations:
        break      
    else:
        print("invalid location")


def mondstadt_city():
    if location in locations == [6]:
        print("welcome to Mondstadt city")
        m = input("do you want to stay or go to another location?:  ")
        if m == "stay":
            mo = input("Do you want to buy things or explore?: ")
        else:
           location = input("what location do you want to explore?:  ").lower()
        if mo == "buy":
            print("You can buy flowers and jewelry ")
            mon = input("What are you going to buy?: ")
        if mo == "explore":
            print("You decided to explore!")
            print("You found some keys for a chest!")
            chest = input("Do you want to continue exploring to find the chest?: ")
        if mon == "flowers":
            print("there are Calla Lilies, Cecilia, Small Lamp Grass, and Windwheel Asters")
            flowers = input("which flower do you want to buy?: ")
        if mon == "jewelry":
            print("there are gems and mora ")
            jewelry  = input("which jewelry do you want to buy?: ")
            if flowers == "Calla Lilies":
                print("You buy some Calla Lilies!")
            if flowers == "Cecilia":
                print("You buy some Cecilias!")
            if flowers == "small Lamp Grass":
                print("You buy some small Lamp Grass!")
            if flowers == "Windwheel Asters":
                print("You buy some Calla Lilies!")
            if jewelry == "gems":
                print("You buy some gems")
            if jewelry == "mora":
                print("You buy some mora")


# define function for Ameno Archon Statue
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can explore
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def statue():
    if location in location:
        print("welcome to the Ameno Archon Statue")
        s = input("do you want to stay or go to another location?:  ")
        if s == "stay":
            st = input("Do you want to explore?: ")
        else:
           location = input("what location do you want to explore?:  ").lower()
        if st == "explore":
            print("You found a sword")
            swo = input("Do you want to keep it?:  ")
        if swo == "yes":
            print("Now you have a new sword")
        if swo == "no":
            print("You left the sword")

# define function for Dawn Winery
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can fight with monsters that are close like a cryo slime or a Hilichurl 
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def winery():
    if location == locations[0]:
        print(f"welcome to Dawn winery")
        w = input("Do you want to stay or go to another location")
        if w == "stay":
            print("You can explore!")
        if w == "another location":
            location = input("what location do you want to explore?:  ").lower()


# define function for Starsnatch Cliff
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can explore to find swords or flowers
    # and they can fight with Hilichurl, slimes, Ruin Guard and eye of the Storm
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def starsnatch():
    if location == locations[1]:
        print("welcome to Starsnatch Cliff")

# define function for Nameless Island
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can explore 
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def island():
     if location ==  locations[2]:
        print("welcome to the Nameless Island")

# define function for Stormbearer Mountains
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can pick up dandelion Seed, and Valberry
    # user can fight with Hilichurl, slimes, Ruin Guard, Cryo abyss mage, Anemo Hypostasis, samachurl, blazing Axe Mitachurl, and Fauti Electro cicin mage.
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def stormbearers():
     if location ==  locations[4]:
        print("Welcome to Stormbearer Mountains")

# define function for Springvale
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can explore 
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def springvale():
    if location ==  locations[5]:
         print("Welcome to Springvale")

# define function for Stormterror’s Lair
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can figth with Hilichurl, abyss mage,  Ruin Guard and Ruin Hunter
    # user can fight with the final boss the dragon Stormterror
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def stormterrors():
    if location ==  locations[7]:
        print("Welcome to Stormterror Lair")

# define function for Starfell Lake  
    # ask user if they want to stay or go to another location
    # if user choose to stay
    # user can explore
    # user can pick up fish 
    # user can figth with hilichurl and samachurl
    # if user choose to go to another location ask what location 
    # if the location is not in the list tell the user that the input is invalid and they need to try again

def starfell():
    if location ==  locations[8]:
        print("Welcome to the Starfell Lake")
        st = input("Do you want to stay or go to another location")
        if st == "stay":
            print("You can pick uo fish or you can explore")
            fish = input("Do you want to pick up fish or explore")

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
        print(f"You used a potion and did {sword_potion} damage!")
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