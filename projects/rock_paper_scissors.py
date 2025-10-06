# NS 1st 🔨 Rock, Paper, Scissors
import random

player_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")
print("Type 'quit' anytime if you want to stop playing.\n")

while True:
    player = input("Enter rock, paper, or scissors: ").lower()

    if player == "quit":
        print("\nThanks for playing!")
        print("Final Score -> You:", player_score, "| Computer:", computer_score)
        break

    if player not in ["rock", "paper", "scissors"]:
        print("Oops! That’s not a valid option, try again.\n")
        continue

    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer picked:", computer)

    if player == computer:
        print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print("Score -> You:", player_score, "| Computer:", computer_score, "\n")
