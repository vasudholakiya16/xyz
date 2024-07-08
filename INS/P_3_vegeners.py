def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key = key.upper()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr(((ord(char.upper()) - ord('A') - shift + 26) % 26) + ord('A'))
            plaintext.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)

def main():
    while True:
        print("Select an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            encryption_key = input("Enter encryption key: ").strip().upper()
            ciphertext = vigenere_encrypt(plaintext, encryption_key)
            print(f"Encrypted: {ciphertext}")
        
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            decryption_key = input("Enter decryption key: ").strip().upper()
            decrypted_text = vigenere_decrypt(ciphertext, decryption_key)
            print(f"Decrypted: {decrypted_text}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()