# NS 1st Elif and Logical Operators notes

grade = 100

if grade > 100:
    print(f"You did extra credit. . . you did {grade - 100}% extra credit!")
elif grade == 100:
    print("Your grade is perfect!")
else: 
    print(f"Try harder you only have {grade}.")

username = "MsLaRose"
password = "1234"

user = input("Enter your username: ")
pword = input("Enter your password: ")

if not user or not pword:
    print("Please enter a valid input")
elif user == "Tia":
    if pword == "password":
        print("Welcome Tia ")
    else:
        print("Password incorrect")
elif user == username and pword == password:
    print("Welcome Ms. LaRose")
elif user == username:
    print("Password incorrect")
else:
    print("Incorrect credentials")