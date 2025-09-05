# NS 1st 🔨 Idiot Proof 

name_input = input("Enter your full name: ")
phone_input = input("Enter your phone number (10 digits): ")
gpa_input = input("Enter your GPA: ") 

formatted_name = name_input.strip().lower().title()

digits = "".join([ch for ch in phone_input if ch.isdigit()])

formatted_phone = f"{digits[0:3]} {digits[3:6]} {digits[6:10]}" 

formatted_gpa = round(float(gpa_input.strip()), 1)

print("\n--- User Information ---")
print("Name:", formatted_name)
print("Phone:", formatted_phone)
print("GPA:", formatted_gpa)