# NS 1st Password Strength Checker


# Ask user what their password is going to be 
password = input("Enter your password: ")

# Check how many points the user has
score = 0

# if the password is 8 characters long user gets one point
if len(password) >= 8:
    score += 1

# if the password contains at least one uppercase letter user gets one point 
if any(char.isupper() for char in password):
    score += 1

# if the password contains at least one lowercase letter user gets one point
if any(char.islower() for char in password):
    score += 1

# if the password contains at least one number user gets one point
if any(char.isdigit() for char in password):
    score += 1

# if the password contains at least one special character user gets one point 
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
if any(char in special_characters for char in password):
    score += 1

# check how many points the user gets 2 = weak, 3 = Moderate, 4 = strong, and 5 = Very strong 
if score <= 2:
    strength = "Weak"
elif score == 3:
    strength = "Moderate"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

# print the password,and how many points the user has 
print(f"\nPassword Strength: {strength}")
print(f"Score: {score}/5")

# if the password is "Weak" the computer will tell the user that the password needs to have more letters, numbers,and special characters.
if strength == "Weak":
    print("Tip: Try adding uppercase letters, numbers, or special characters.")
# if the password is "Moderate" the computer will tell the user that is almost strong but it needs more things in the password 
elif strength == "Moderate":
    print("Almost there! Add more variety or length to make it stronger.")
