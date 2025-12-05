# NS 1st Final Project code 

locations = ["dawn winery", "starsnatch cliff", "nameless island", "ameno archon statue", 
             "stormbearer mountains", "springvale", "mondstadt city", "stormterror's lair", "starfell lake"]

print(locations)

location = input("what location do you want to explore?: ").lower()
if location == locations:
        print(f"Time to explore {location}")
else:
        print("Invdalid location try again")


def Mondstadtcity():
    if location == locations[6]:
        print("welcome to Mondstadt city")

def anemo_archon_statue():
    if location == locations[3]:
        print("welcome to the Ameno Archon Statue")

def dawn_winery():
    if location == locations[0]:
        print("welcome to Dawn Winery")

def starsnatch_cliff():
    if location == locations[1]:
        print("welcome to Starsnatch Cliff")

def nameless_island():
     if location == locations[2]:
        print("welcome to the Nameless Island")

def stormbearer_mountains():
     if location == locations[4]:
        print("Welcome to Stormbearer Mountains")

def springvale():
    if location == locations[5]:
         print("Welcome to Springvale")

def stormterrors_lair():
    if location == locations[7]:
        print("Welcome to Stormterror Lair")

def starfell_lake():
    if location == locations[8]:
        print("Welcome to the Starfell Lake")

