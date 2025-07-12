# Function to encrypt the message
def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Leave non-letters unchanged
    return result

# Function to decrypt the message
def decrypt(message, shift):
    return encrypt(message, -shift)

# Main program
def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (number): "))
    except ValueError:
        print("Please enter a valid number for shift.")
        return

    if choice == 'e':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice! Please enter 'e' or 'd'.")

# Run the program
if __name__ == "__main__":
    main()
