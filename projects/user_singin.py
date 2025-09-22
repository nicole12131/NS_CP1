# NS 1st 🔨 User Sign In

username = ("neily.salom")
password = ("1234567")
user_name = ("neilyx")
pass_word = ("876543")

username_one = input("Enter username: ")
password_one = input("Enter password: ")
username_two = input("Enter username: ")
password_two = input("Enter password: ")


if username_one == username:
    if password_one == password:
        print(f"Welcome {username_one}")
    else:
        print("Password invalid try again!")
if username_two == user_name:
    if password_two == pass_word:
        print(f"Welcome {username_two}")
    else:
        print("Password invalid try again!")
else:
    print("Username invalid try again!")