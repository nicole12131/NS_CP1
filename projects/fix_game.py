# NS 1st 🔨 Fix the Game

import random 

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # Bug 1: The input is a string but should be an integer for comparison.
        # This caused a TypeError when comparing `guess` to `number_to_guess`.
        # Fix: Use int() to convert the input string to an integer.
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            # Bug 2: Invalid input should not count as an attempt.
            # Fix: Use `continue` to restart the loop without incrementing attempts.
            continue
            
        attempts += 1
        
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempts} attempts!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
            
        # Bug 3: The attempts counter and game over condition were checked out of order.
        # This meant the "out of attempts" message would only show after the final guess.
        # Fix: The attempts check needs to be placed *after* the guess but *before* the next turn.
        # Moved the `attempts >= max_attempts` check to the correct place.
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        
        # Bug 4: The `continue` statement at the end of the loop was unnecessary.
        # It forced the loop to restart even after a correct guess.
        # It's removed to allow the game to end and print the "Game Over" message.
        # Fix: Remove the unnecessary `continue` statement.
        
    print("Game Over. Thanks for playing!")

start_game()