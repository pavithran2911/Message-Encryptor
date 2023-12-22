def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value for encryption: "))

    encrypted_message = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")
