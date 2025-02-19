def encrypt(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetical characters remain unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with negative shift

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Choose an option: \n1. Encrypt\n2. Decrypt\nYour choice: ")
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == '1':
        encrypted_text = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_text}")
    elif choice == '2':
        decrypted_text = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_text}")
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
