# NS 1st 🔨 Idiot Proof 

name = input("What is your name?").strip().capitalize()
last_name = input("What is your last name?").strip().capitalize()
phone_number = input("What is your phone number?").strip()
email = input("What is your email address?").strip()
gpa = input("What is your GPA?").strip()

print(f"Full Name: {name} {last_name} " )
print(f"Phone Number: {phone_number}")
print(f"Email Address: {email}")
print(f"GPA: {gpa :1f}")
print(gpa.isdecimal())


