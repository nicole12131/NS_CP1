# NS 1st 🔨 Cesar Cypher encoder and decoder

# 1. Display a menu asking user to choose operation (encode or decode)
# 2. Get the user's choice (1 for encode, 2 for decode)
# 3. Ask for the message to encode/decode
# 4. Ask for the shift value (integer)
# 5. Define a function 'caesar_cipher' that:
#       - Takes text, shift value, and mode ('encode' or 'decode')
#       - Shifts letters by 'shift' positions
#       - Wraps around A-Z or a-z if needed
#       - Leaves non-alphabetic characters unchanged
# 6. Call the function with user input and display the result

# FUNCTION DEFINITIONS


def caesar_cipher(text, shift, mode):
    result = ""

    # Reverse shift if decoding
    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if it's a letter
            # Determine ASCII base (A or a)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap using modulo 26
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Leave non-alphabetic characters unchanged
            result += char

    return result


def main():
    print("Choose operation (1 for encode, 2 for decode): ", end="")
    choice = input().strip()

    # Validate choice
    if choice not in ['1', '2']:
        print("Invalid choice! Please enter 1 or 2.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == '1':
        encoded = caesar_cipher(message, shift, "encode")
        print(f"\nEncoded message: {encoded}")
    else:
        decoded = caesar_cipher(message, shift, "decode")
        print(f"\nDecoded message: {decoded}")


# Run the program
if __name__ == "__main__":
    main()
