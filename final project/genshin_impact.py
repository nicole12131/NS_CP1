# NS 1st Final Project code 

locations = ["Dawn winery", "Starsnatch cliff", "Nameless Island", "Ameno Archon Statue", 
             "Stormbearer Mountains", "Springvale", "Mondstadt City", "Stormterror's Lair", "Starfell Lake"]

location = input("what location do you want to explore?: ")
def location_mondstadt():
    if location == locations:
        print(f"Time to explore {location}")
    if location != locations:
        print("Invdalid location try again")