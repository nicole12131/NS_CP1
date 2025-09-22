# NS 1st 🔨 User Sign In

correct_username = "neily.salom"
correct_password = "1234567"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Welcome to the program,", username + "!")
else:
    print("Invalid login credentials. Please try again.")