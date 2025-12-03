# NS 1st Project Pseudocode

# create a list that shows all of the locations of the game 

# define a function that allows the user to choose a location in the list
    # ask user what location they want to explore
    # if the location that the user choose is on the list it will return the location to the main game loop and it will continue the game
    # if the location is not in the list tell the user that the input is invalid and they need to try again

# define a function for all of the locations so the user could explore them and pick up things from there
    # if the player is in that location for the first time they can pick up things
    # if the player is in that location for the second time they can't pick up things that they have in the inventory that means that they need to find things that they never pick up or they need to go to another location
    # if the player pick up a new item the item is send to the inventory list

# create a function that runs the combats 
    # the user has four options punch, sword, use a potion or run away 
    # if the user choose to punch they make 1-3 of damage
    # if the user choose sword they make 3-6 of damage
    # if the user choose potion they can see the inventory to choose a potion 
    # if the user choose to run away they need to choose a location 
    # inside of the function create a loop that repeats the combat 
        # if the player has 0 of HP he dies and he need to restart the game
        # if the abyss mage has 0 of HP the player wins and he can continue the game
        # if the drangon has 0 of HP the player wins the dragon is now on their side and the player can continue the game

# create a list that has all of the items that the player has pick up

#  define a function that shows the player's inventory
    # the user has two options use an item or remove item from inventory 
    # if the player choose to use an item he can choose one of the items
    # if the items is not in the inventory the user need to try again
    # if the item is on the inventory they can use it and have the effect of that item
    # if the player decides to remove an item 
    # if that item is not in the inventory the user needs to try again
    # if the item is on the inventory the items is remove from the inventory 

# Create a loop that increases the player's stats 
    # if the player level up all of the stats increases 
    # if the player complete a quest the magic, and defense increases
    # if the player complete a quest the user gets new items to use 
    # if the player gain experience the attack, HP and defense increases 

# create a loop that triggers when the player dies 
    # if user has 0 of HP the game will end 
    # print a "You have died" message 
    # ask user if they want to restart the game
    # if user choose to restart the game will start again 
    # if the player decides not to restart the game ends
    # print "thanks for playing this game"