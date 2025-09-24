# NS 1st 🔨 What is My Grade

percentage = float(input("Enter your grade percentage:  "))


if percentage >= 93:
    print(f"You have a {percentage}%, which is an A.")
elif percentage >= 90:
    print(f"You have a {percentage}%, which is an A-.")
elif percentage >= 87:
    print(f"You have a {percentage}%, which is a B+.")
elif percentage >= 83:
    print(f"You have a {percentage}%, which is a B.")
elif percentage >= 80:
    print(f"You have a {percentage}%, which is a B-.")
elif percentage >= 77:
    print(f"You have a {percentage}%, which is a C+.")
elif percentage >= 73:
    print(f"You have a {percentage}%, which is a C.")
elif percentage >= 70:
    print(f"You have a {percentage}%, which is a C-.")
elif percentage >= 67:
    print(f"You have a {percentage}%, which is a D+.")
elif percentage >= 63:
    print(f"You have a {percentage}%, which is a D.")
elif percentage >= 60:
    print(f"You have a {percentage}%, which is a D-.")
else:
    print(f"You have a {percentage}%, which is an F.")
 