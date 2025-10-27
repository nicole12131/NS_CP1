# NS 1st Combate Program 
import random

print("Welcome to training! First I need to know some thimgs about you!")

name = input("Enter your name: ")
class_fighter = input("Enter your class of fighter(1 for fighter, 2 for Mage, 3 for Rouge):  ")

if class_fighter == 1:
    print("Defense: 15")
    print("Attack: 20 + 5")
    print("Damage: 9 + 3")
elif class_fighter == 2:
    print("Defense: 3")
    print("Attack: 15 + 3")
    print("Damage: 5 + 3")
else:
    print("Defense: 18")
    print("Attack: 20 + 7")
    print("Damage: 9 + 6")

player_health = 100
monster_health = 100
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
    
monster_health, player_health = damage(10, "player")
print(f"Monster Health: {monster_health}")
print(f"Player Health: {player_health}")